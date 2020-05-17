from twilio.twiml.messaging_response import MessagingResponse
#API para se comunicar com o WhatsApp

from controller.classifier import Classifier

class WhatsappClassifier():

    def whatsapp_reply(self, sample):

        REALLY_TRUTH_URL = "https://i.pinimg.com/originals/83/2b/34/832b34e5e61f5e7d45da478f2c545e53.gif"
        MAYBE_TRUTH_URL = "https://media.tenor.com/images/1dd2bc5ce366262629bd8d7d6b0e674a/tenor.gif"
        MAYBE_FALSE_URL = "https://loonylabs.files.wordpress.com/2016/08/dog-staring-at-cupcakes-gif.gif"
        REALLY_FALSE_URL = "https://4.bp.blogspot.com/-0RRfcGdCTiI/VquKv3DhdmI/AAAAAAAB1oo/HdknqIR9tl0/s1600/5a991a2337f9dbd0feb3f648264c421c.gif"

        # Classificador
        cl = Classifier('./models/')
        result = cl.make_classification(sample)

        # Define a imagem
        media = REALLY_TRUTH_URL
        media = MAYBE_TRUTH_URL if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA FALSA' else media
        media = MAYBE_FALSE_URL if result[0] == 'ESSA NOTICIA PARECE VERDADEIRA' else media
        media = REALLY_FALSE_URL if result[0] == 'NAO SEI, ESSA NOTICIA TALVEZ SEJA VERDADEIRA' else media

        # Cria a resposta
        resp = MessagingResponse()
        msg = resp.message(str(result[0]))
        msg.media(media)

        return str(resp)

# Cria um bot "eco" para WhatsApp
# Para acessá-lo a pessoa deve enviar a mensagem "join around-south" sem aspas para o número +1 415 523 8886
# Podemos automatizar isso com um botão que possua a URL https://api.whatsapp.com/send?phone=+14155238886&text=join+around-south
