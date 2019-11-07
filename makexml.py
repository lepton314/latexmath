import xml.etree.ElementTree as et
sqrtcount = 0
fraccount = 0


def makexml(formula, parent):
    IVcount = 0
    global sqrtcount
    global fraccount
    for element in formula:
        if 'type' in element:
            underover = et.SubElement(parent, 'munderover')
            underelement = et.SubElement(underover,element['tag'])
            underelement.text = element['name']
            brakets_x = et.SubElement(underover ,'mrow')
            makexml(element['indexvalue1'], brakets_x)
            brakets_y = et.SubElement(underover, 'mrow')
            makexml(element['indexvalue2'], brakets_y)
        elif 'indexkey1' in element and 'sub' == element['indexkey1']:
            sub = et.SubElement(parent, 'msub')
            if 'function' == element['mode']:
                function = et.SubElement(sub, 'mi')
                function.text = element['name']
                makexml(element['indexvalue1'], sub)
                Inti = et.SubElement(parent, 'mo')
                Inti.text = '\u2062'
            else:
                subelement = {}
                for key, value in element.items():
                    if key == 'indexkey1':
                        continue
                    subelement[key] = value
                makexml([subelement], sub)
                makexml(element['indexvalue1'], sub)
        elif 'indexkey2' in element and 'sup' == element['indexkey2']:
            sup = et.SubElement(parent, 'msup')
            if 'function' == element['mode']:
                function = et.SubElement(sup, 'mi')
                function.text = element['name']
                makexml(element['indexvalue2'], sup)
                Inti = et.SubElement(parent, 'mo')
                Inti.text = '\u2062'
            else:
                subelement = {}
                for key, value in element.items():
                    if key == 'indexkey2':
                        continue
                    subelement[key] = value
                makexml([subelement], sup)
                makexml(element['indexvalue2'], sup)
        elif 'sqrt' == element['mode']:
            sqrtcount += 2
        elif 'frac' == element['mode']:
            fraccount += 2
            frac = et.SubElement(parent, 'mfrac')
        elif 'subformula' == element['mode']:
            if '1' == element['tag']:
                brakets_a = et.SubElement(parent, 'mfenced')
                brakets_b = et.SubElement(brakets_a, 'mrow')
                makexml(element['children'], brakets_b)
            elif '2' == element['tag']:
                if sqrtcount == 2:
                    sqrtcount -= 2
                    sqrt = et.SubElement(parent, 'msqrt')
                    brakets = et.SubElement(sqrt, 'mrow')
                    makexml(element['children'], brakets)
                elif sqrtcount == 1:
                    sqrtcount -= 1
                    brakets = et.SubElement(mroot, 'mrow')
                    makexml(element['children'], brakets)
                elif fraccount > 0:
                    fraccount -= 1
                    brakets = et.SubElement(frac, 'mrow')
                    makexml(element['children'], brakets)
                else:
                    brakets = et.SubElement(parent, 'mrow')
                    makexml(element['children'], brakets)
            elif '3' == element['tag']:
                sqrtcount -= 1
                mroot = et.SubElement(parent, 'mroot')
                brakets = et.SubElement(mroot, 'mrow')
                makexml(element['children'], brakets)
            elif '4' == element['tag']:
                brakets_a = et.SubElement(
                    parent, 'mfenced', {'open': "{"}, {'close': "}"})
                brakets_b = et.SubElement(brakets_a, 'mrow')
                makexml(element['children'], brakets_b)
        elif 'operator2' == element['mode']:  # 演算子
            IVcount = 0
            operator = et.SubElement(parent, 'mo')
            operator.text = element['name']
        elif 'operator3' == element['mode']:  # 演算子
            IVcount = 0
            operator = et.SubElement(parent, 'mo')
            operator.text = element['name']
        elif 'function' == element['mode']:
            IVcount = 0
            function = et.SubElement(parent, 'mi')
            function.text = element['name']

            Inti = et.SubElement(parent, 'mo')
            Inti.text = '\u2062'
        elif 'symbol' == element['mode']:  # 二項関係記号
            IVcount = 0
            symbol = et.SubElement(parent, 'mo')
            symbol.text = element['name']
        elif 'frac' == element['mode']:  # 二項関係記号
            IVcount = 0
            symbol = et.SubElement(parent, 'mo')
            symbol.text = element['name']
        elif 'greek' == element['mode']:  # 二項関係記号
            IVcount = 0
            symbol = et.SubElement(parent, 'mo')
            symbol.text = element['name']
        elif 'arrows' == element['mode']:  # 二項関係記号
            IVcount = 0
            symbol = et.SubElement(parent, 'mo')
            symbol.text = element['name']
        elif 'number' == element['mode']:  # 数字
            number = et.SubElement(parent, 'mn')
            number.text = element['name']
            IVcount += 1
        else:
            if IVcount >= 1:
                Inti = et.SubElement(parent, 'mo')
                Inti.text = '\u2062'
                IVcount -= 1
                characters = et.SubElement(parent, 'mi')
                characters.text = element['name']
                IVcount += 1
            else:
                characters = et.SubElement(parent, 'mi')
                characters.text = element['name']
                IVcount += 1
