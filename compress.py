import os
from PIL import Image


TARGET = '1. target'
COMPRESSED = '2. compressed'

if not os.path.exists(COMPRESSED):
    os.mkdir(COMPRESSED)

for root, dirs, files in os.walk(TARGET):
    print(dirs)
    path = root.split
    for f in files:
        subdir = os.path.split(root)[1]
        subdir = os.path.join(COMPRESSED, subdir)
        if not os.path.exists(subdir):
            os.mkdir(subdir)
        extension = os.path.splitext(f)[1]
        # print(extension)
        if extension == '.JPG':
            filepath = os.path.join(root, f)
            print("compressed: ", filepath)
            im = Image.open(filepath)
            width, height = im.size

            im2 = im.resize((int(width/4), int(height/4)))

            newpath = os.path.join(subdir, f)
            print(">>", newpath)
            im2.save(newpath)