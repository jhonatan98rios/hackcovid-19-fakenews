import nltk
nltk.data.path.append('./models/')
import nlpnet
nlpnet.set_data_dir('./models/pos-pt/')
from xml.etree import ElementTree as ET
import requests
import metadata_parser

nltk.download('punkt')

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
        titles = [title.text for title in tree.findall('channel/item/title')[:3]]
        return (titles, links)

    def get_img_url(self, links):
        img_url = []
        for link in links:
            try:
                metadata = metadata_parser.MetadataParser(link, search_head_only=True)
                img_link = metadata.get_metadata_link('image')
                img_url.append(img_link)
            except:
                img_url.append('')
        return img_url

    def build_dict(self, text):
        kw = self.get_keywords(text)
        titles, links = self.find_news(kw)
        imgs = self.get_img_url(links)
        
        array = [dict(), dict(), dict()]
        
        if(links and titles and imgs):
            for i in range(len(links)):
                array[i] = {
                    'link': links[i],
                    'title': titles[i],
                    'img': imgs[i]
                }
            return array
        else:
            return "Error to get news"
        

