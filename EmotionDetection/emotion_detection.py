import requests
import json

def emotion_detector(text_to_analyze):
    # Check if the input is blank
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Original code for emotion detection
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
    
    if response.status_code == 400:  # Handle error response from Watson API
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_dict = response.json()  # Parse the response to a dictionary
    
    # Extracting emotion scores
    emotion_data = response_dict['emotionPredictions'][0]['emotion']
    
    # If any emotion data is missing, handle gracefully
    anger_score = emotion_data.get('anger', None)
    disgust_score = emotion_data.get('disgust', None)
    fear_score = emotion_data.get('fear', None)
    joy_score = emotion_data.get('joy', None)
    sadness_score = emotion_data.get('sadness', None)
    
    # Find the dominant emotion
    dominant_emotion = max(emotion_data, key=emotion_data.get, default=None)
    
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
