# -*- coding: utf-8 -*-
from xml.etree.ElementTree import *


def main():
    mrow = Element('mrow')
    msqrt = SubElement(mrow, 'msqrt')
    msqrt.text = "Liechtenstein"

    rank = SubElement(mrow, 'rank')
    rank.text = "2"
    rank.set('updated', 'yes')
    year = SubElement(mrow, 'year')
    year.text = "2019"
    neighbor = SubElement(mrow, 'neighbor')
    name = SubElement(neighbor, 'name')
    name.text = "Austria"

    dump(mrow)


if __name__ == '__main__':
    main()
