from flask import Flask, render_template, request
import requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion_Detection")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    anger = response['anger']
    disgust = response['disgust'] 
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is <b>{dominant_emotion}</b>."


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
