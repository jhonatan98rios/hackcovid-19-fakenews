import os
from flask import Flask, jsonify, request
#from flask_cors import CORS

from controller.classifier import Classifier
from controller.whatsapp import WhatsappClassifier

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify({"message": "Hello World"})


# Main classifier
@app.route("/news_validator", methods=['POST'])
def news_validator():

    if request.json:
        cl = Classifier('./models/')
        sample = request.json["sample"]
        result = cl.make_classification(sample)
        json = { 'result': result[0], "percentage": result[1] }
    else:
        json = { 'result': 'Error', "percentage": "Error" }

    return json


# Whatsapp message sender
@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():

    if request:
        if request.form:
            sample = request.form.get('Body')
        elif request.json:
            sample = request.json["sample"]
        wc = WhatsappClassifier()
        result = wc.whatsapp_reply(sample)
        json = { 'result': result[0], "percentage": result[1] }
    else:
        json = { 'result': 'Error', "percentage": "Error" }

    return json


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)