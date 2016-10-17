__author__ = 'benjaminpower'

from PIL import Image

img = Image.open("image.png")

if img.size == (1920, 1080):
    for x in xrange(img.size[0]):
        for y in xrange(img.size[0]):
            img.point(range(0, 0, 0))











