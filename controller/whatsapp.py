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


        return result

# Cria um bot "eco" para WhatsApp
# Para acessá-lo a pessoa deve enviar a mensagem "join around-south" sem aspas para o número +1 415 523 8886
# Podemos automatizar isso com um botão que possua a URL https://api.whatsapp.com/send?phone=+14155238886&text=join+around-south
