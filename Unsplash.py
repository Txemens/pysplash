
import requests
import json
import os
import urllib.request
import asyncio
from pathlib import Path

class Unsplash():
    url = "https://api.unsplash.com/"
    acceskey = ""
    headers = {}
    photoUrl = ''
    photoid = ''
    photoFile = ''
    filepath =''

    def __init__(self, parameter_list):
        self.headers = {"Authorization": "Client-ID "+self.acceskey}

    def getRandom(self, parameter_list):
        url = self.url+"photos/random"
        r = requests.get(url, headers=self.headers)
        resp = r.json()
        self.photoUrl = resp['urls']['full']
        self.photoid = resp['id']

    @asyncio.coroutine
    def save_image(self):
        home = str(Path.home())
        self.filepath =  home+'/Downloads/unsplash-'+self.photoid+'.jpg'
        print(self.filepath)
        self.photoFile = open(self.filepath,"w+")
        r = urllib.request.urlretrieve(self.photoUrl,self.filepath )
    
    def changeBackground(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.save_image())
        s = os.system("gsettings set org.gnome.desktop.background picture-uri "+self.filepath)
        print("gsettings set org.gnome.desktop.background picture-uri "+self.filepath)