from twilio.twiml.messaging_response import MessagingResponse
#API para se comunicar com o WhatsApp

from controller.classifier import Classifier
from controller.news import NewsSearch

class WhatsappClassifier():

    def whatsapp_builder(self, sample, resp):
        ns = NewsSearch()
        news = ns.build_dict(sample)
        message = f'\n *{str(resp)}*'

        for i in range(3):
            message = message + '\n\n' + news["title"][i] + '\n' + news["url"][i]
            
        return str(message)


    def whatsapp_reply(self, sample):

        REALLY_TRUTH_URL = "https://i.imgur.com/FQpbutt.png"
        MAYBE_TRUTH_URL = "https://i.imgur.com/IHJ1fNs.png"
        MAYBE_FALSE_URL = "https://i.imgur.com/dcHwOE1.png"
        REALLY_FALSE_URL = "https://i.imgur.com/NrSoyyC.png"

        # Classificador
        cl = Classifier('./models/')
        result = cl.make_classification(sample)

        # Define a imagem
        media = REALLY_TRUTH_URL
        media = MAYBE_TRUTH_URL if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA VERDADEIRA' else media
        media = MAYBE_FALSE_URL if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA FALSA' else media
        media = REALLY_FALSE_URL if result[0] == 'ESSA NOTICIA PARECE FALSA' else media


        # Cria a resposta
        wp = self.whatsapp_builder(sample, result[0])
        resp = MessagingResponse()
        msg = resp.message(wp)
        msg.media(media)

        return str(resp)

# Cria um bot "eco" para WhatsApp
# Para acessá-lo a pessoa deve enviar a mensagem "join around-south" sem aspas para o número +1 415 523 8886
# Podemos automatizar isso com um botão que possua a URL https://api.whatsapp.com/send?phone=+14155238886&text=join+around-south
