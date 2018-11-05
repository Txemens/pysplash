#! /usr/bin/env python3

from Unsplash import Unsplash

splash = Unsplash('test')

splash.getRandom("")

splash.save_image()

splash.changeBackground()