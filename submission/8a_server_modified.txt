"""Serve the Emotion Detector web application using Flask."""

from flask import Flask, render_template, request
from requests.exceptions import RequestException

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the supplied text and format emotion scores for the web page."""
    text_to_analyse = request.args.get("textToAnalyze", "")
    try:
        result = emotion_detector(text_to_analyse)
    except (RequestException, ValueError, KeyError, IndexError, TypeError):
        return "Emotion detection service is unavailable. Please try again later.", 503

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


@app.route("/")
def index():
    """Render the emotion analysis form."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
