#!/usr/bin/env python3

from Unsplash import Unsplash

# insert your Unsplash Access Key below
access_key = ''
# add the tags to the list
# Example:
#       tags = ['space','nature','forest']

tags = []


splash = Unsplash(access_key)
splash.set_tags(tags)
splash.set_random_background()
