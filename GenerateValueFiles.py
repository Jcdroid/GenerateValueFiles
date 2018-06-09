__author__ = 'caojing'

import os
import math

width_base = 320
height_base = 480
xml_head = '<?xml version="1.0" encoding="utf-8"?>'
folder = 'res/values-{0}x{1}'
name_x = 'lay_x.xml'
name_y = 'lay_y.xml'
label1 = '<resources>'
label_x = '<dimen name=\"x{0}\">{1}px</dimen>'
label_y = '<dimen name=\"y{0}\">{1}px</dimen>'
label2 = '</resources>'

screen = [(320, 480), (480, 800), (480, 854), (540, 960), (600, 1024),
          (720, 1184), (720, 1196), (720, 1280),
          (768, 1024), (768, 1280), (800, 1280),
          (1080, 1812), (1080, 1920), (1440, 2560)]

def generateDefaultXmlFile():
    for x, y in screen:
        generateXmlFile(x, y)

def generateXmlFile(width, height):
    realFolder = folder.format(height, width)
    if not os.path.exists(realFolder):
        os.makedirs(realFolder)

    lay_x = open(realFolder+'/'+name_x, 'w')
    lay_x.write(xml_head)
    lay_x.write('\n')
    lay_x.write(label1)
    for x in range(1, width_base+1, 1):
        lay_x.write('\n\t')
        lay_x.write(label_x.format(x, math.ceil(x*width)/math.ceil(width_base)))
    lay_x.write('\n')
    lay_x.write(label2)
    lay_x.close()

    lay_y = open(realFolder+'/'+name_y, 'w')
    lay_y.write(xml_head)
    lay_y.write('\n')
    lay_y.write(label1)
    for y in range(1, height_base+1, 1):
        lay_y.write('\n\t')
        lay_y.write(label_y.format(y, math.ceil(y*height)/math.ceil(height_base)))
    lay_y.write('\n')
    lay_y.write(label2)
    lay_y.close()

if __name__=='__main__':
    generateDefaultXmlFile()