#モジュール読み込み
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
        if '\(' in elements:
            parsed_elements.append({'mode': 'operator1','name': '\('})
        elif '\)' in elements:
            parsed_elements.append({'mode': 'operator1','name': '\)'})
        elif '\\sin' in elements:
            parsed_elements.append({'mode': 'function','name': 'sin'})
        elif '\\cos' in elements:
            parsed_elements.append({'mode': 'function','name': 'cos'})
        elif '\\tan' in elements:
            parsed_elements.append({'mode': 'function','name': 'tan'})
        elif '\+' in elements:
            parsed_elements.append({'mode': 'operator2','name': '\+'})
        elif '\pm' in elements:
            parsed_elements.append({'mode': 'operator2','name': '\+'})
        elif '\-' in elements:
            parsed_elements.append({'mode': 'operator2','name': '\-'})
        elif '=' in elements:
            parsed_elements.append({'mode': 'equal','name': '='})
        else:
            parsed_elements.append({'mode': 'number','value': element})
            parsed_formulas.append(parsed_elements)
    print(parsed_formulas)


#xmlに変換
mathmls = []
math = et.Element('math')
tree = et.ElementTree(element=math)
for formulas in parsed_formulas:
    #括弧などの特殊処理
    if 'operator1' in formulas.get('mode'): 
    #括弧閉じが来るまでループさせる
    if 'operator2' in formulas.get('mode'):　#演算子
        operator = et.SubElement(math,'mo')
        operator.text = formulas.get('name')
    elif 'equal' in formulas.get('mode'):　#演算子
        equal = et.SubElement(math,'mo')
        equal.text = formulas.get('name')
    elif 'number' in formulas.get('mode'): #英数字
        if str.isdecimal(formulas.get('value')):#数字のみ
            number = et.SubElement(math,'mn')
            mn.text = formulas.get('value')
        else:
            temp = re.search(r'\d+',forlamus.get('value')) #混在した場合の数字の取り出し。
            number = et.SubElement(math,'mn')
            mn.text = temp
            temp2 = list(re.search('[^0-9]+',forlamus.get('value')))#英字部分取り出し
            for String in temp2:
                Inti = et.SubElement(math,'mo')
                Inti.text = '&InvisibleTimes;'
                string = et.SubElement(math,'mi')
                string.text = String
        
tree.write('test.xml', encoding='utf-8', xml_declaration=True) #