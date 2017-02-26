import os
import math
from PIL import Image

go = True

def tryread(obj):
    r = obj.read(1)

    if r != "":
        return 255-ord(r)
    else:
        global go
        go = False
        print "err"
        return 255-0



file = "file.mp3"
f = open(file, "rb")
l1=[]
l2=[]
fs = os.path.getsize(file)/4
print "File size",fs,"Bytes"
w = int(math.sqrt(fs))
im = Image.new("RGBA", (w+1, w+1), "white")
i=0




try:
    while go:
        r,g,b,a = tryread(f),tryread(f),tryread(f),tryread(f)
        im.putpixel((i//(w+1),i%(w+1)),(r,g,b,a))
        i+=1
finally:
    im.save("out.png")
    f.close()


'''
1 1 0
0 1 1
1 0 1
0 0 0
'''