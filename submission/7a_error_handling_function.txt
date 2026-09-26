"""Detect emotions in English text using the Watson NLP service."""

import json

import requests


EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyse):
    """Return five emotion scores and the dominant emotion, or None for invalid text.

    Connection failures and non-400 HTTP failures propagate to the caller so
    service outages are not incorrectly reported as invalid user input.
    """
    empty_result = dict.fromkeys((*EMOTIONS, "dominant_emotion"))
    if not text_to_analyse.strip():
        return empty_result

    response = requests.post(
        EMOTION_URL,
        json={"raw_document": {"text": text_to_analyse}},
        headers={
            "grpc-metadata-mm-model-id":
                "emotion_aggregated-workflow_lang_en_stock"
        },
        timeout=20,
    )
    if response.status_code == 400:
        return empty_result
    response.raise_for_status()

    scores = json.loads(response.text)["emotionPredictions"][0]["emotion"]
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result
