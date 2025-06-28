import requests
import json 

def emotion_detector(text_to_analyse):
    url='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url=url, json=obj, headers=headers).text
    formatted_response= json.loads(response)
    return formatted_response