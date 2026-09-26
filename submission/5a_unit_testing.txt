"""Course emotion checks against the real Watson NLP endpoint (network required)."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Verify the dominant emotion for each of the five course examples."""

    def test_joy(self):
        """A glad statement should express joy."""
        self.assertEqual(emotion_detector(
            "I am glad this happened")["dominant_emotion"], "joy")

    def test_anger(self):
        """An angry statement should express anger."""
        self.assertEqual(emotion_detector(
            "I am really mad about this")["dominant_emotion"], "anger")

    def test_disgust(self):
        """A disgusted statement should express disgust."""
        self.assertEqual(emotion_detector(
            "I feel disgusted just hearing about this")["dominant_emotion"], "disgust")

    def test_sadness(self):
        """A sad statement should express sadness."""
        self.assertEqual(emotion_detector(
            "I am so sad about this")["dominant_emotion"], "sadness")

    def test_fear(self):
        """An afraid statement should express fear."""
        self.assertEqual(emotion_detector(
            "I am really afraid that this will happen")["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main(verbosity=2)
