from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renders the provided HTML page

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_api():
    statement = request.args.get('textToAnalyze')
    result = emotion_detector(statement)  # Call the emotion detection function

    # Check if dominant_emotion is None (error case)
    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again."}), 400  # Return 400 status and error message

    return jsonify(result)  # Return the emotion detection result




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
