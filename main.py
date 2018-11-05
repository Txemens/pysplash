#!/usr/bin/env python3

#pip install requests

from Unsplash import Unsplash

# insert your Unsplash Access Key below
access_key = ''

splash = Unsplash(access_key)
splash.set_random_background()
