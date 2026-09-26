"""Exercise real parsing and Flask routes with only HTTP calls mocked."""

import json
import unittest
from unittest.mock import Mock, patch

import requests

from EmotionDetection.emotion_detection import emotion_detector
from server import app


SCORES = {"anger": 0.01, "disgust": 0.02, "fear": 0.03,
          "joy": 0.90, "sadness": 0.04}
EMPTY = {"anger": None, "disgust": None, "fear": None,
         "joy": None, "sadness": None, "dominant_emotion": None}


def response(status=200):
    """Build an HTTP response fixture using the Watson response envelope."""
    result = Mock(status_code=status)
    payload = {
        "emotionPredictions": [{"emotion": dict(SCORES),
                                "target": "", "emotionMentions": []}]
    }
    result.text = json.dumps(payload)
    return result


class DetectorContractTests(unittest.TestCase):
    """Catch score parsing, request contract and status handling regressions."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_scores_and_dominant_emotion(self, post):
        post.return_value = response()
        self.assertEqual(emotion_detector("I love this new technology."),
                         {**SCORES, "dominant_emotion": "joy"})
        self.assertEqual(post.call_args.kwargs["json"],
                         {"raw_document": {"text": "I love this new technology."}})
        self.assertEqual(post.call_args.kwargs["headers"], {
            "grpc-metadata-mm-model-id":
                "emotion_aggregated-workflow_lang_en_stock"})
        self.assertGreater(post.call_args.kwargs["timeout"], 0)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_dominant_emotion_is_selected_from_scores(self, post):
        post.return_value = response()
        payload = json.loads(post.return_value.text)
        payload["emotionPredictions"][0]["emotion"] = {
            "anger": 0.8, "disgust": 0.02, "fear": 0.05,
            "joy": 0.03, "sadness": 0.1}
        post.return_value.text = json.dumps(payload)
        self.assertEqual(emotion_detector("I am angry.")["dominant_emotion"],
                         "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400_returns_none_for_every_field(self, post):
        post.return_value = response(400)
        self.assertEqual(emotion_detector("invalid"), EMPTY)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input_is_invalid_even_without_network(self, post):
        post.side_effect = AssertionError("Blank input must not call Watson")
        for value in ("", "  \n\t"):
            with self.subTest(value=value):
                self.assertEqual(emotion_detector(value), EMPTY)

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_service_failure_is_not_invalid_text(self, post):
        post.return_value = response(503)
        post.return_value.raise_for_status.side_effect = requests.HTTPError()
        with self.assertRaises(requests.HTTPError):
            emotion_detector("Hello")


class ServerContractTests(unittest.TestCase):
    """Catch missing routes, swallowed service failures and bad result formatting."""

    def setUp(self):
        self.client = app.test_client()

    def test_home_page_contains_input_and_result(self):
        result = self.client.get("/")
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'id="textToAnalyze"', result.data)
        self.assertIn(b'id="system_response"', result.data)

    def test_missing_empty_and_whitespace_input(self):
        for query in ({}, {"textToAnalyze": ""}, {"textToAnalyze": " \t"}):
            with self.subTest(query=query):
                result = self.client.get("/emotionDetector", query_string=query)
                self.assertEqual(result.status_code, 200)
                self.assertEqual(result.text, "Invalid text! Please try again!")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_formatted_result(self, post):
        post.return_value = response()
        result = self.client.get("/emotionDetector", query_string={
            "textToAnalyze": "I am happy & excited!"})
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.text,
                         "For the given statement, the system response is "
                         "'anger': 0.01, 'disgust': 0.02, 'fear': 0.03, "
                         "'joy': 0.9 and 'sadness': 0.04. "
                         "The dominant emotion is joy.")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_watson_400_is_shown_as_invalid_input(self, post):
        post.return_value = response(400)
        result = self.client.get("/emotionDetector?textToAnalyze=invalid")
        self.assertEqual(result.text, "Invalid text! Please try again!")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_timeout_returns_retryable_error(self, post):
        post.side_effect = requests.Timeout()
        result = self.client.get("/emotionDetector?textToAnalyze=Hello")
        self.assertEqual(result.status_code, 503)
        self.assertIn("unavailable", result.text)


if __name__ == "__main__":
    unittest.main()
