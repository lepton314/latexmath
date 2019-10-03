import re
import xml.etree.ElementTree as et

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

    trimmed_formula = re.sub('\s','',formula)
    elements = re.sub('(\+|-|=|\(|\))',r'/\1/',trimmed_formula).split('/')
    print(formula)
    print(trimmed_formula)
    print(elements)
    parsed_elements = []
    for element in elements:
        if '\\sin' in elements:
            parsed_elements.append({'mode': 'function','name': 'sin'})
        elif '\\cos' in elements:
            parsed_elements.append({'mode': 'function','name': 'cos'})
        elif '\\tan' in elements:
            parsed_elements.append({'mode': 'function','name': 'tan'})
        elif '\+' in elements:
            parsed_elements.append({'mode': 'operator','name': '\+'})
        elif '\-' in elements:
            parsed_elements.append({'mode': 'operator','name': '\-'})
        elif '\=' in elements:
            parsed_elements.append({'mode': 'equal','name': '\='})
        else:
            parsed_elements.append({'mode': 'number','value': element})
            parsed_formulas.append(parsed_elements)
#xmlに変換
mathmls = []
math = et.Element('math')
tree = et.ElementTree(element=math)
for formulas in parsed_formulas:
    if 'operator' in formulas.keys('mode'):
        operator = et.SubElement(math,'mo')
        mo.text = formulas.get('name')
    elif 'number' in formulas.keys('mode'):
        if str.isdecimal(formulas.get('value'):
            number = et.SubElement(math,'mn'):
            mn.text = formulas.get('value')