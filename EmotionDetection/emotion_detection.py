import requests
import json 

def emotion_detector(text_to_analyse):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, json=obj, headers=headers)
    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    emotion= json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion, key = emotion.get)
    return {
        'anger': emotion['anger'],
        'disgust': emotion['disgust'],
        'fear': emotion['fear'],
        'joy': emotion['joy'],
        'sadness': emotion['sadness'],
        'dominant_emotion': dominant_emotion
    }
    