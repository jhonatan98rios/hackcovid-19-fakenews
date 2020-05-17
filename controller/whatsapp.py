from twilio.twiml.messaging_response import MessagingResponse
#API para se comunicar com o WhatsApp

from controller.classifier import Classifier

class WhatsappClassifier():

    def whatsapp_reply(self, sample):

        # Classificador
        cl = Classifier('./models/')
        result = cl.make_classification(sample)

        # Cria a resposta
        resp = MessagingResponse()
        resp.message(str(result))


        return resp


    def whatsapp_reply_2(self, sample):

        #Imagens provisórias para o retorno via Whatsapp
        happy_dog_url = "https://t1.ea.ltmcdn.com/pt/images/4/2/0/cachorro_feliz_recomendacoes_gerais_23024_orig.jpg"
        #sad_dog_url = "https://i.pinimg.com/originals/e4/a5/33/e4a533fca82e142230182129793682b6.jpg"

        resp = MessagingResponse()

        cl = Classifier('./models/')
        result = cl.make_classification(sample)
        
        msg = resp.message(result[0])
        msg.media(happy_dog_url)
    # Tentei fazer com que, se a notícia fosse falsa, aparecesse a imagem do cachorro triste, mas está difícil :(
         

        return str(resp)











# Cria um bot "eco" para WhatsApp
# Para acessá-lo a pessoa deve enviar a mensagem "join around-south" sem aspas para o número +1 415 523 8886
# Podemos automatizar isso com um botão que possua a URL https://api.whatsapp.com/send?phone=+14155238886&text=join+around-south
