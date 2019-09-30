import sys  #因数の読み取り
import re   #正規表現
from xml.etree.ElementTree import *

def finder(s):
    if '\sin' in s:
         mrow = Element('mrow')
         msup = SubElement(mrow,'msup')
         mi = SubElement(msup, 'mi')
         mi.text = "sin"
         mo = SubElement(mrow, "mo")
         mo.text = "&ApplyFunction;"
         dump(mrow)
fp = open(sys.argv[1], 'r')
for line in fp.readlines():
    finder(line)
fp.close()
