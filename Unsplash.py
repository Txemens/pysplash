import requests
import json
import os
import urllib.request
import asyncio
from pathlib import Path

class Unsplash():
    url = "https://api.unsplash.com/"
    headers = None
    photoUrl = None
    photoid = None
    photoFile = None
    filepath =None
    tags = None
    background_commands = {
        'mate': 'gsettings set org.mate.background picture-filename ',
        'gnome': 'gsettings set org.gnome.desktop.background picture-uri file://'
    }

    def __init__(self, access_key):
        self.headers = {"Authorization": "Client-ID " + access_key}

    def get_random_image(self):
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

    def change_background(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.save_image())
        background_command = self.get_background_command()
        s = os.system(background_command + self.filepath)
        print(background_command + self.filepath)

    def get_background_command(self):
        uses_gnome_command = ['budgie-desktop']
        desktop_environment = os.environ['DESKTOP_SESSION'].lower()

        if desktop_environment in self.background_commands:
            command = self.background_commands[desktop_environment]
        elif desktop_environment in uses_gnome_command:
            command = self.background_commands['gnome']
        else:
            raise Exception('Sorry, your desktop environment is not supported currently.')

        return command

    def set_random_background(self):
        self.get_random_image()
        self.save_image()
        self.change_background()

    def create_url(self):
        self.url = self.url+"photos/random"
        if self.tags is not None:
            self.url = self.url+"?query="+self.tags
