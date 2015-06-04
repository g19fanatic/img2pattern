#!/usr/bin/env python

import sys, os
from PIL import Image

def rgb2hex(r, g, b): #curtosy of http://stackoverflow.com/a/19917486/496405
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        imgPath = sys.argv[1]
        imgDir,imgName = os.path.split(imgPath)
        im = Image.open(imgPath)
        im = im.convert('RGB')
        xsize,ysize = im.size
        lines=[]
        colors = []

        outputTxt = '<html><body><table><tr><td>'

        for y in reversed(range(ysize)):
            currentLine = []
            for x in range(xsize):
                curColor = im.getpixel((x,y))
                if curColor not in colors:
                    colors.append(curColor)
                currentLine.append(str(colors.index(curColor)+1))
            lines.append(currentLine)

        for line in reversed(lines):
            outputTxt += ",".join(line)
            outputTxt += '<br/>'
        outputTxt += "</td><td><img src='file://%s' /></td></tr></table>" % (imgPath)


        outputTxt += "<div>There are %s colors: <br/><ol>" % (len(colors))
        for i, color in enumerate(colors):
            if len(color) < 4:
                r,g,b = color
            else:
                r,g,b,a = color
            hexTxt = rgb2hex(r,g,b)
            outputTxt += "<li><span style='background-color: %s;' >%s</span></li>" % (hexTxt,hexTxt)

        outputTxt += '</ol></div></body></html>'

        print outputTxt

        open('%s%simg2pattern_output.html' % (imgDir,os.sep), "w").write(outputTxt)

    else:
        print "Must add a path to an image"
