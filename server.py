'''
Server for Emotional Detection
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion_Detection")

@app.route("/emotionDetector")
def emotion_detect():
    '''
    Emotional detector
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    if response['anger'] is None:
        return " Invalid text! Please try again!."
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    return (
    f"For the given statement, the system response is 'anger': {anger}, "
    f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
    f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    '''
    Rendering html page
    '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
