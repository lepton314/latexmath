def makeindexformula(formula):
    input_formula = [element for element in formula]
    built_formula = []
    while(True):
        if input_formula is None or len(input_formula) == 0:
            break
        element = input_formula[0]
        input_formula = input_formula[1:]
        if 'subformula' == element['mode']:
            element['children'] = makeindexformula(element['children'])
            built_formula.append(element)
        elif 'sub' == element['mode']:
            built_formula[-1]['indexkey1'] = 'sub'
            built_formula[-1]['indexvalue1'] = makeindexformula([input_formula[0]])
            input_formula = input_formula[1:]
        elif 'sup' == element['mode']:
            built_formula[-1]['indexkey2'] = 'sup'
            built_formula[-1]['indexvalue2'] = makeindexformula([input_formula[0]])
            input_formula = input_formula[1:]
        else:
            built_formula.append(element)        
    return (built_formula)
