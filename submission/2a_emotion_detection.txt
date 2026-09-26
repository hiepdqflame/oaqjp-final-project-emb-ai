"""Task 2: return the raw Watson response before adding output formatting."""

import requests


def emotion_detector(text_to_analyze):
    """Submit English text to Watson NLP and return the raw JSON response text."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    response = requests.post(
        url,
        json={"raw_document": {"text": text_to_analyze}},
        headers=headers,
        timeout=20,
    )
    response.raise_for_status()
    return response.text
