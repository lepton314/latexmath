#モジュール読み込み
import re
import xml.etree.ElementTree as et
from parse import parse_element

#ファイル読み込み
with open('input.tex','r') as f:
    raw_text = f.read()
    formulas = raw_text.split('\n')

#データ整形
fixed_formulas = []
for formula in formulas:
    if formula != '':
        fixed_formulas.append(formula)

#パース
parsed_formulas = []
for formula in fixed_formulas:

    trimmed_formula = re.sub('\s','/',formula)
    split_rule = r'(\\[A-z]+|\+|-|=|\(|\)|\{|\}|_|\^|[0-9]+|[a-z])'
    elements_with_empty = re.sub(split_rule,r'/\1/',trimmed_formula).split('/')
    elements = []
    for element in elements_with_empty:
        if len(element) > 0:
            elements.append(element)
    #print(formula)
    #print(trimmed_formula)
    #print(elements)
    parsed_elements = []
    for element in elements:
        parse_element(element, parsed_elements)
    parsed_formulas.append(parsed_elements)
    print(parsed_formulas)
#Subformula
built_formulas = []
built_formula = []
for formula in parsed_formulas:
    for element in formula:
        built_formula.append(element)
    print(formula) 
    print(built_formula)
    built_formulas.append(built_formula)
#xmlに変換
xmlcount = 0
for formula in parsed_formulas:
    root = et.Element('math')
    tree = et.ElementTree(element=root)
    brakets = 0
    IVcount = 0
    for element in formula:
        #括弧などの特殊処理
        if 'brakets1' in element['mode']:
            if brakets == 0:
                braket = et.SubElement(root,'mfenced')
                braketop = et.SubElement(braket,'mrow')
            brakets += 1
        elif 'brakets2' in element['mode']:
            brakets -= 1
        elif 'brakets3' in element['mode']:
            brakets += 1
        elif 'brakets4' in element['mode']:
            brakets -= 1
        elif 'brakets5' in element['mode']:
            brakets += 1
        elif 'brakets6' in element['mode']:
            brakets -= 1
        elif 'sqrt' in element['mode']:
            sqrtcount += 1
            sqrt = et.SubElement(root,'msqrt')
        elif 'root' in element['mode']:
            rootcount += 1
        elif 'frac' in element['mode']:
            fraccount += 1
        elif 'sub' in element['mode']:
            subcount += 1
        elif 'sup' in element['mode']:
            supcount += 1        
        elif brakets == 0:
            if 'operator2' in element['mode']:#演算子
                IVcount = 0
                operator = et.SubElement(root,'mo')
                operator.text = element['name']
            elif 'function' == element['mode']:
                IVcount = 0
                function = et.SubElement(root,'mi')
                function.text = element['name']
                Inti = et.SubElement(root,'mo')
                Inti.text = '&InvisibleTimes;'
            elif 'symbol'in element['mode']: #二項関係記号
                IVcount = 0
                symbol = et.SubElement(root,'mo')
                symbol.text = element['name']
            elif 'number' in element['mode']: #数字
                number = et.SubElement(root,'mn')
                number.text = element['value']
                IVcount += 1
            else:
                if IVcount >= 1: 
                    Inti = et.SubElement(root,'mo')
                    Inti.text = '&#x2062;<!--INVISIBLE TIMES-->'
                    IVcount -= 1
                characters = et.SubElement(root,'mi')
                characters.text = element['value']
                IVcount += 1           
    xmlcount += 1
    tree.write('output/math' + str(xmlcount) + '.xml', encoding='utf-8', xml_declaration=True) #xmlとしての書き出し
