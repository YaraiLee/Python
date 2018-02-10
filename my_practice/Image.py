# -*- coding: utf-8 -*-

from PIL import Image
im = Image.open('logo.png')
im.show()
print(im.format, im.size, im.mode)

im.thumbnail((20, 10))
im.save('logo_small.jpg', 'JPEG')
im.show()