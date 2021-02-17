# Made with ♥ by Federico Gerardi

import requests
from bs4 import BeautifulSoup


class Vquesrs:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    def __init__(self, url):
        self.url = url

    def is_there_text_by_id(self, text, id):
        """
        Is there the text inside that id? True or False
        """
        request = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(request.text, 'html.parser')

        if text in str(soup.find(id=id)):
            return True
        else:
            return False

    def get_text_by_id(self, id):
        """
        Can I get the text inside that id? Sure :)
        """
        request = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(request.text, 'html.parser')

        return str(soup.find(id=id))

    def send_discord_hook(self, url, content, username='', avatar_url='', tts=False):
        """
        Send a discord webhook :D
        """
        data = {"content": content}

        if username:
            data['username'] = username
        
        if avatar_url:
            data['avatar_url'] = avatar_url
        
        if tts:
            data['tts'] = 'true'

        requests.post(url, data=data)