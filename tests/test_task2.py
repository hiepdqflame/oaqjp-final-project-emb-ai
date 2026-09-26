"""Verify the original task 2 raw-response contract separately from task 3."""

import unittest
from unittest.mock import Mock, patch

from stages.task2.emotion_detection import emotion_detector


class Task2Tests(unittest.TestCase):
    """The first task must return response.text without output formatting."""

    @patch("stages.task2.emotion_detection.requests.post")
    def test_raw_response_is_returned(self, post):
        post.return_value = Mock(text='{"emotionPredictions": []}')
        self.assertEqual(emotion_detector("I love this new technology."),
                         '{"emotionPredictions": []}')
