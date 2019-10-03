import re
#import xml.etree.ElementTree as et

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
        else:
            parsed_elements.append({'mode': 'number','value': element})
            parsed_formulas.append(parsed_elements)
    
#xmlに変換
#mathmls = []
for formulas in parsed_formulas:
    if 'mode' in formulas.keys('number'):
        



