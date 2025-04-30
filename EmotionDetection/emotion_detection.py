import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=input_json)
    response_dict = response.json()  # Parse the response to a dictionary
    
    # Extracting emotion scores
    emotion_data = response_dict['emotionPredictions'][0]['emotion']
    anger_score = emotion_data['anger']
    disgust_score = emotion_data['disgust']
    fear_score = emotion_data['fear']
    joy_score = emotion_data['joy']
    sadness_score = emotion_data['sadness']
    
    # Find the dominant emotion
    dominant_emotion = max(emotion_data, key=emotion_data.get)
    
    # Returning the formatted output
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }

if __name__ == "__main__":
    text_to_analyze = "I am so happy I am doing this."
    emotion_data = emotion_detector(text_to_analyze)
    print(emotion_data)
