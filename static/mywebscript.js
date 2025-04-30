let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                let response = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML =
                    `For the given statement, the system response is '${response.dominant_emotion}': ${response[response.dominant_emotion]}, with other emotions like 'anger': ${response.anger}, 'disgust': ${response.disgust}, 'fear': ${response.fear}, and 'sadness': ${response.sadness}.`;
            } else if (this.status == 400) {
                let errorResponse = JSON.parse(xhttp.responseText);  // Parse error response
                document.getElementById("system_response").innerHTML = errorResponse.error;  // Display error message
            }
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
