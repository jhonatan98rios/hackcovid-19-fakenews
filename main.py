import os
from flask import Flask, jsonify, request
#from flask_cors import CORS

from controller.classifier import Classifier
from controller.news import NewsSearch
from databases.db import DBConnection

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify({"percentage": 0.7572562842863373, "results": "ESSA NOTICIA PARECE FALSA"})


# Main classifier
@app.route("/news_validator", methods=['POST'])
def news_validator():

    cl = Classifier('./models/')
    ns = NewsSearch()

    if request.json:
        sample = request.json["sample"]
        result = cl.make_classification(sample)
        news = ns.build_dict(sample)

        # Define a cor
        color = 4
        color = 3 if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA VERDADEIRA' else color
        color = 2 if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA FALSA' else color
        color = 1 if result[0] == 'ESSA NOTICIA PARECE FALSA' else color
        json = { 'result': result[0], 'percentage': result[1], 'news': news, 'type': color }
    else:
        json = { 'result': 'Error', 'percentage': 'Error', 'news': 'Error' }

    return json

# Database access
@app.route("/save_news", methods=['POST'])
def save_news():

    if request.json:
        try:
            sample = request.json["sample"]
            print(sample)
            db = DBConnection()
            db.save_sample(sample)

            return "Salvo com sucesso"
        except:
            return "Erro ao salvar"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)