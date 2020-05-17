from flask import Flask, jsonify, request
#from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse
#API para se comunicar com o WhatsApp

from databases.db import DBConnection
from controller.classifier import Classifier

app = Flask(__name__)
#CORS(app)

#Imagens provisórias para o retorno via Whatsapp
happy_dog_url = "https://t1.ea.ltmcdn.com/pt/images/4/2/0/cachorro_feliz_recomendacoes_gerais_23024_orig.jpg"
sad_dog_url = "https://i.pinimg.com/originals/e4/a5/33/e4a533fca82e142230182129793682b6.jpg"

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

    resp = MessagingResponse()
    msg1 = 'Essa noticia parece falsa'
    msg2 = 'Nao sei, essa noticia talvez seja falsa'
    if request.form:
        sample = request.form.get('Body')
    else:
        sample = request.json["sample"]
    cl = Classifier('./models/')
    result = cl.make_classification(sample)
    json = { 'result': result[0], "percentage": result[1] }
    msg = resp.message(result[0])
    msg.media(happy_dog_url)
   # Tentei fazer com que, se a notícia fosse falsa, aparecesse a imagem do cachorro triste, mas está difícil :(
    if result[0] == 'ESSA NOTICIA PARECE SER FALSA':
       msg.media(sad_dog_url)
    if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA FALSA':
       msg.media(sad_dog_url)    

    return str(resp)


# Return all users from database
@app.route('/get_users', methods=['GET'])
def get_users():

    db = DBConnection()
    data = db.read_all()
    return jsonify(data)


# Create a new user in database
@app.route('/create_user', methods=['POST'])
def new_user():

    if request.json:
        db = DBConnection()
        name = request.json["name"]
        job = request.json["job"]
        db.create_user(name, job)
        message = { "text": "Success" }
    else:
        message = { "text": "Fail" }

    return jsonify(message)


# Retorna um hello World simples para testar se o app esta funcionando
@app.route('/', methods=['GET'])
def hello():

    hello = "Hello World!!"

    result = {
        "percentage": 0.5536440125152253,
        "result": "ESSA NOTICIA PARECE VERDADEIRA"
    }

    return jsonify(result)
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
