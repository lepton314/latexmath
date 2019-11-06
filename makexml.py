import xml.etree.ElementTree as et
sqrtcount = 0
fraccount = 0
def makexml(formula,parent):
    IVcount = 0
    global sqrtcount
    global fraccount
    for element in formula:
        if 'sqrt' in element['mode']:
            sqrtcount += 2
        elif 'frac' in element['mode']:
            fraccount += 2
            frac = et.SubElement(parent,'mfrac')
        elif 'subformula' in element['mode']:
            if '1' == element['tag']:
                brakets_a = et.SubElement(parent,'mfenced')
                brakets_b = et.SubElement(brakets_a,'mrow')
                makexml(element['children'],brakets_b)
            elif '2' == element['tag']:
                if sqrtcount == 2:
                    sqrtcount -= 2
                    sqrt = et.SubElement(parent,'msqrt')
                    brakets = et.SubElement(sqrt,'mrow')
                    makexml(element['children'],brakets)
                elif sqrtcount == 1:
                    sqrtcount -= 1
                    makexml(element['children'],mroot)
                elif fraccount == 2: 
                    fraccount -= 1
                    makexml(element['children'],frac)
            elif '3' == element['tag']:
                if sqrtcount == 2:
                    sqrtcount -=1
                    mroot = et.SubElement(parent,'mroot')
                    makexml(element['children'],mroot)                    
        elif 'operator2' in element['mode']:#演算子
            IVcount = 0
            operator = et.SubElement(parent,'mo')
            operator.text = element['name']
        elif 'operator3' in element['mode']:#演算子
            IVcount = 0
            operator = et.SubElement(parent,'mo')
            operator.text = element['name']
        elif 'function' == element['mode']:
            IVcount = 0
            function = et.SubElement(parent,'mi')
            function.text = element['name']
            Inti = et.SubElement(parent,'mo')
            Inti.text = '&InvisibleTimes;'
        elif 'symbol'in element['mode']: #二項関係記号
            IVcount = 0
            symbol = et.SubElement(parent,'mo')
            symbol.text = element['name']
        elif 'frac'in element['mode']: #二項関係記号
            IVcount = 0
            symbol = et.SubElement(parent,'mo')
            symbol.text = element['name']
        elif 'greek'in element['mode']: #二項関係記号
            IVcount = 0
            symbol = et.SubElement(parent,'mo')
            symbol.text = element['name']            
        elif 'number' in element['mode']: #数字
            number = et.SubElement(parent,'mn')
            number.text = element['value']
            IVcount += 1
        else:
            if IVcount >= 1: 
                Inti = et.SubElement(parent,'mo')
                Inti.text = '&#x2062;<!--INVISIBLE TIMES-->'
                IVcount -= 1
                characters = et.SubElement(parent,'mi')
                characters.text = element['value']
                IVcount += 1
            else:    
                characters = et.SubElement(parent,'mi')
                characters.text = element['value']
                IVcount += 1
