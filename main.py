import argparse
import os
import math
from PIL import Image
from time import gmtime, strftime

go = True


def stamp(mode=0):
    # 0 = info
    # 1 = warn
    # 2 = error
    msg = "INFO"
    if mode == 0:
        msg = "INFO"
    elif mode == 1:
        msg = "WARN"
    elif mode == 2:
        msg = "ERRO"
    return strftime("[" + msg + " %H:%M:%S" + "]", gmtime())

def tryread(obj):
    r = obj.read(1)

    if r != "":
        return 255-ord(r)
    else:
        global go
        go = False
        return 255-0



def main():
    print stamp(),"Initiating"
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output Filename", type=str)
    parser.add_argument("-i", "--input", help="Input Filename", type=str)
    args = parser.parse_args()
    if args.input:
        file = args.input
        print stamp(), "Searching for the file", args.input
        if (os.path.isfile(args.input)):
            print stamp(), "The file", args.input, "Found"
            f = open(file, "rb")
            fs = os.path.getsize(file) / 4
            print stamp(),"Input file size", fs, "Bytes"
            w = int(math.sqrt(fs))
            im = Image.new("RGBA", (w + 1, w + 1), "white")
            i = 0
            print stamp(),"Generating", w+1,"x",w+1, "PNG image"
            try:
                while go:
                    r, g, b, a = tryread(f), tryread(f), tryread(f), tryread(f)
                    im.putpixel((i // (w + 1), i % (w + 1)), (r, g, b, a))
                    i += 1
            finally:
                filename = "output"
                if args.output:
                    print stamp(0),"Image will be saved as",args.output+".png"
                    filename = args.output
                else:
                    print stamp(1),"Image will be saved as output.png as no output filename specified"

                try:
                    print stamp(),"Attempting to save image as",filename+".png"
                    im.save(filename + ".png", optimize=True, quality=100, mode="RGB")
                except:
                    print stamp(2), "Unable to write the output image to disk as", filename + ".png"
                    print stamp(), "Exiting Program"
                    return
                print stamp(), "Generated Image Successfully Saved!"
                print stamp(), "Closing all opened files"
                f.close()
                print stamp(), "Exiting Program"
            return
        else:
            print stamp(2), "The file", args.input, "was not found"
            print stamp(), "Exiting program"
            return
    else:
        print stamp(2),"Input File not specified"
        print stamp(), "Exiting program"
        return


main()




'''
1 1 0
0 1 1
1 0 1
0 0 0
'''