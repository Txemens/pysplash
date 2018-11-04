#! /usr/bin/env python3

#pip install requests

from Unsplash import Unsplash


splash = Unsplash('test')

splash.getRandom("")

splash.save_image()

splash.changeBackground()