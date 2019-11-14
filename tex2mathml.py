#モジュール読み込み
import re
import xml.etree.ElementTree as et
from parse import parse_element
from subformula import makesubformula
from indexformula import makeindexformula
from makexml import makexml

#ファイル読み込み
with open('test.tex','r') as f:
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
    split_rule = r'(\\[A-Za-z]+|\+|-|=|\(|\)|\\?\{|\\?\}|_|\^|\[|\]|\||[0-9]+|[a-z])'
    elements_with_empty = re.sub(split_rule,r'/\1/',trimmed_formula).split('/')
    elements = []
    for element in elements_with_empty:
        if len(element) > 0:
            elements.append(element)
    print(formula)
    #print(trimmed_formula)
    print(elements)
    parsed_elements = []
    for element in elements:
        parse_element(element, parsed_elements)
    parsed_formulas.append(parsed_elements)
    #print(parsed_formulas)


#Subformula
built_formulas = []
for formula in parsed_formulas:
    modified_formula, _ = makesubformula(formula)
    #print(formula) 
    # print(modified_formula)
    print('{')
    for row in modified_formula:
        print(row)
    print('}')
    built_formulas.append(modified_formula)
print('-----------------------------------------------------------')
#indexformula
built_formulas2 = []
for formula in built_formulas:
    modified_formula2 = makeindexformula(formula)
    #print(formula)
    #print(modified_formula2)
    print('{')
    for row in modified_formula2:
        print(row)
    print('}')
    built_formulas2.append(modified_formula2)

#xmlに変換
xmlcount = 0
for formula in built_formulas2:
    root = et.Element('math',{'xmlns':'http://www.w3.org/1998/Math/MathML'})
    
    tree = et.ElementTree(element=root)    
    makexml(formula,root)     
    xmlcount += 1
    tree.write('output/math' + str(xmlcount) + '.xml', encoding='utf-8', xml_declaration=True) #xmlとしての書き出し
