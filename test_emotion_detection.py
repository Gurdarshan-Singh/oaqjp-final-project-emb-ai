import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result1 = emotion_detector("I am glad this happened")['dominant_emotion']
        self.assertEqual(result1,"joy")
        result1 = emotion_detector("I am really mad about this")['dominant_emotion']
        self.assertEqual(result1,"anger")
        result1 = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        self.assertEqual(result1,"disgust")
        result1 = emotion_detector("I am so sad about this")['dominant_emotion']
        self.assertEqual(result1,"sadness")
        result1 = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual(result1,"fear")

if __name__ == '__main__':
    unittest.main()