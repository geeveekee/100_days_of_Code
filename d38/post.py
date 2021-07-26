from logging import setLogRecordFactory
import requests
from icecream import ic
url = requests.get('https://api.npoint.io/1e40766612527b92eb09')

class Post:
    
    def __init__(self, index):
        self.item = index
        self.post_content = url.json()[self.item]
        self.id = self.post_content["id"]
        self.title = self.post_content["title"]
        self.subtitle = self.post_content["subtitle"]
        self.body = self.post_content["body"]

