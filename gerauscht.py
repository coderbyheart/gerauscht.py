#!/usr/bin/env python2

from PIL import Image
import sys
from random import random

src = Image.open(sys.argv[1] if len(sys.argv) > 1 else "cbh.png")
outfile = sys.argv[2] if len(sys.argv) > 2 else "out.png"
srcpix = src.load()
HEIGHT, WIDTH = src.size

out = Image.new("RGB", src.size, (255, 255, 255))
outpix = out.load()

for x in range(src.size[0]):
    for y in range(src.size[1]):
        p = srcpix[x, y]
        greyValue = int((srcpix[x, y][0] + srcpix[x, y][1] + srcpix[x, y][2]) / 3)
        
        colorPossibility = greyValue / float(255)
                
        # grey = int(255 - 255 * random() * colorPossibility * colorPossibility)
        haspixel = 255 if random() > colorPossibility * colorPossibility else 0
        
         
        grey = int(random() * colorPossibility * 255) if haspixel else int((1 - random() * (1 - colorPossibility)) * 255)
        colorpixel = True if haspixel > 0 and random() > 0.85 else False
        # tacker blau
	# color = (grey, grey, grey) if not colorpixel else (56,158,252)
	# cbh rot
	color = (grey, grey, grey) if not colorpixel else (215,42,42)
        outpix[x, y] = color
        
out.save(outfile, "PNG")

print "Done."
