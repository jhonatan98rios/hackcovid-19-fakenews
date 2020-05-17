from twilio.twiml.messaging_response import MessagingResponse
#API para se comunicar com o WhatsApp

from controller.classifier import Classifier
from controller.news import NewsSearch

class WhatsappClassifier():

    def whatsapp_builder(self, sample, resp):
        ns = NewsSearch()
        news = ns.build_dict(sample)
        message = ''

        for i in range(3):
            message = message + news["title"][i] + '\n' + news["url"][i] + '\n\n'
            
        return str(message)


    def whatsapp_reply(self, sample):

        REALLY_TRUTH_URL = "https://t1.ea.ltmcdn.com/pt/images/4/2/0/cachorro_feliz_recomendacoes_gerais_23024_orig.jpg"
        MAYBE_TRUTH_URL = "https://dummyimage.com/300x300/000/6fa.jpg"
        MAYBE_FALSE_URL = "https://dummyimage.com/300x300/000/fc3.jpg"
        REALLY_FALSE_URL = "https://i.pinimg.com/originals/e4/a5/33/e4a533fca82e142230182129793682b6.jpg"

        # Classificador
        cl = Classifier('./models/')
        result = cl.make_classification(sample)

        # Define a imagem
        media = REALLY_TRUTH_URL if result[0] == 'ESSA NOTICIA PARECE VERDADEIRA' else 'https://dummyimage.com/300x300/000/fff.jpg'
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
