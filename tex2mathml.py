import re


with open('test.tex','r') as f:
    raw_text = f.read()
    formulas = raw_text.split('\n')

fixed_formulas = []
for formula in formulas:
    if formula != '':
        fixed_formulas.append(formula)


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
            parsed_elements.append({'mode': 'function','value': element})
            parsed_formulas.append(parsed_elements)
        
