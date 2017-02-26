import os
import math
from PIL import Image

go = True

def tryread(obj):
    r = obj.read(1)

    if r != "":
        return ord(r)
    else:
        global go
        go = False
        print "err"
        return 0



file = "file.mp3"
f = open(file, "rb")
l1=[]
l2=[]
fs = os.path.getsize(file)/3
print "File size",fs,"Bytes"
w = int(math.sqrt(fs))
im = Image.new("RGBA", (w+1, w+1), "white")
i=0




try:
    while go:
        r,g,b,a = tryread(f),tryread(f),tryread(f),255
        # print i
        im.putpixel((i//(w+1),i%(w+1)),(r,g,b,a))
        i+=1
finally:
    im.save("out.png")
    f.close()