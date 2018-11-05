
import requests
import json
import os
import urllib.request
import asyncio
from pathlib import Path

class Unsplash():
    url = "https://api.unsplash.com/"
    acceskey = "eaf1ab9d483e2f771082c65cba70293744a9682ce3f796cb8844c655039481b7"
    headers = None
    photoUrl = None
    photoid = None
    photoFile = None
    filepath =None
    tags = None

    def __init__(self, parameter_list):
        self.headers = {"Authorization": "Client-ID "+self.acceskey}

    def getRandom(self, parameter_list):
        self.createUrl()
        print(self.url)
        r = requests.get(self.url, headers=self.headers)
        resp = r.json()
        print(resp)
        self.photoUrl = resp['urls']['full']
        self.photoid = resp['id']

    @asyncio.coroutine
    def save_image(self):
        home = str(Path.home())
        self.filepath =  home+'/Downloads/unsplash-'+self.photoid+'.jpg'
        self.photoFile = open(self.filepath,"w+")
        r = urllib.request.urlretrieve(self.photoUrl,self.filepath )
    
    def changeBackground(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.save_image())
        s = os.system("gsettings set org.gnome.desktop.background picture-uri 'file:///"+self.filepath+"'")

    def createUrl(self):
        self.url = self.url+"photos/random"
        if self.tags is not None:
            self.url = self.url+"?query="+self.tags
        
            