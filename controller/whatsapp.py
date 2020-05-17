from twilio.twiml.messaging_response import MessagingResponse
#API para se comunicar com o WhatsApp

from controller.classifier import Classifier

class WhatsappClassifier():

    def whatsapp_reply(self, sample):

        REALLY_TRUTH_URL = "https://t1.ea.ltmcdn.com/pt/images/4/2/0/cachorro_feliz_recomendacoes_gerais_23024_orig.jpg"
        MAYBE_TRUTH_URL = "https://t1.ea.ltmcdn.com/pt/images/4/2/0/cachorro_feliz_recomendacoes_gerais_23024_orig.jpg"
        REALLY_FALSE_URL = "https://i.pinimg.com/originals/e4/a5/33/e4a533fca82e142230182129793682b6.jpg"
        MAYBE_FALSE_URL = "https://i.pinimg.com/originals/e4/a5/33/e4a533fca82e142230182129793682b6.jpg"

        # Classificador
        cl = Classifier('./models/')
        result = cl.make_classification(sample)

        # Define a imagem
        media = REALLY_TRUTH_URL
        media = MAYBE_TRUTH_URL if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA FALSA' else media
        media = REALLY_FALSE_URL if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA VERDADEIRA' else media
        media = MAYBE_FALSE_URL if result[0] == 'ESSA NOTICIA PARECE VERDADEIRA' else media

        # Cria a resposta
        resp = MessagingResponse()
        msg = resp.message(str(result))
        msg.media(media)

        return str(resp)

# Cria um bot "eco" para WhatsApp
# Para acessá-lo a pessoa deve enviar a mensagem "join around-south" sem aspas para o número +1 415 523 8886
# Podemos automatizar isso com um botão que possua a URL https://api.whatsapp.com/send?phone=+14155238886&text=join+around-south
