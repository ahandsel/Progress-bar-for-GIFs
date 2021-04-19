#!/usr/bin/env python
__author__ = "@ustundag"
__author2__ = "@ahandsel"

import sys, math, numpy
from PIL import Image
import imageio
import datetime

# Color input as REG
# Gray = (153, 153, 153)
# Soft Blue = 172, 219, 242
bar_color = (172, 219, 242)

def processImage(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print("File not found! ", infile)
        sys.exit(1)

    i = 0
    print("Processing your gif...")
    mypalette = im.getpalette()
    frames = []
    try:
        while 1:
            im.putpalette(mypalette)
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            frames.append(new_im)
            i += 1
            im.seek(im.tell() + 1)
    except EOFError:
        pass # end of frames
    
    return frames

print("Looking good so far...")
gif_file = sys.argv[1]
frames = processImage(gif_file)
frame_count = len(frames)
im = Image.open(gif_file)
size = im.size
bar_size = math.ceil(size[0]/frame_count)
x_pos = 0
y_pos = size[1] - bar_size
progress_frames = []

print("Now adding the progress bar...")
i = 0
for im in frames:
    frame_bar = Image.new('RGBA', (bar_size+(bar_size*i), bar_size), bar_color)
    im.paste(frame_bar, (x_pos, y_pos))
    progress_frames.append(numpy.array(im))
    i += 1

print("Almost there...")
now = datetime.datetime.now()
timeStamp = "% s" % now.year + "_" + "% s" % now.month + "_" + "% s" % now.day + "_" + "% s" % now.hour + "% s" % now.minute

new_filename = timeStamp + '_edited_' + sys.argv[1]
imageio.mimwrite(new_filename, progress_frames)
print("GIF with progress bar created, ", new_filename)
