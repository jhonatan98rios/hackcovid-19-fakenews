import nltk
nltk.data.path.append('./models/')
import nlpnet
nlpnet.set_data_dir('../models/pos-pt/')
from xml.etree import ElementTree as ET
import requests
import nltk

class NewsSearch():

    def __init__(self):
        self.tagger = nlpnet.POSTagger()

    def get_keywords(self, text):
        first = text.split('.')[0]
        tags = self.tagger.tag(first)
        keywords = [word[0] for word in tags[0] if (word[1] == 'NPROP' and len(word[0]) >=2)][:4]
        if len(keywords) < 3:
            keywords.extend([word[0] for word in tags[0] if word[1] == 'N' or word[1] == 'ADJ'][:3])
        return keywords

    def find_news(self, keywords):
        url = 'https://news.google.com/rss/search?q={}&hl=pt-BR&gl=BR&ceid=BR:pt-419'.format(" ".join(w for w in keywords))
        response = requests.get(url)
        tree = ET.fromstring(response.content)
        links = [link.text for link in tree.findall('channel/item/link')[:3]]
        print(links)
        return links

