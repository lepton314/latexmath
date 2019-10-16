def makesubformula(formula):
    input_formula = [element for element in formula]
    built_formula = []
    rack_elements = None
    while(True):
        if input_formula is None or len(input_formula) == 0:
            break
        element = input_formula[0]
        input_formula = input_formula[1:]
        if 'brackets1' in element['mode']:
            sub_built, sub_rack = makesubformula(input_formula)
            input_formula = sub_rack
            built_formula.append({
                'mode': 'subformula','tag':'1',
                'children': sub_built
            })
        elif 'brackets3' in element['mode']:
            sub_built, sub_rack = makesubformula(input_formula)
            input_formula = sub_rack
            built_formula.append({
                'mode': 'subformula','tag':'2',
                'children': sub_built
            })
        elif 'brackets5' in element['mode']:
            sub_built, sub_rack = makesubformula(input_formula)
            input_formula = sub_rack
            built_formula.append({
                'mode': 'subformula','tag':'3',
                'children': sub_built
            })
        elif 'brackets2' in element['mode'] or 'brackets4' in element['mode'] or 'brackets6' in element['mode']:
            rack_elements = input_formula
            break
        else:
            built_formula.append(element)        
    return (built_formula, rack_elements)


# def makesubformula(element, built_formula,sub_formula,brakets_a,brakets_b,brakets_c):
#     if 'brakets1' in element['mode']:
#         brakets_a += 1
#     elif brakets_a >= 1:
#         sub_formula[brakets_a].append(element)
#     elif 'brakets2' in element['mode']:
#         if brakets_a == 0:
#             built_formula.append({'mode': 'subformula','tag': 'mrow','value':sub_formula[brakets_a]})
#         brakets_a -= 1
#     elif 'brakets3' in element['mode']:
#         brakets_b += 1
#     elif brakets_b >= 1:
#         sub_formula[brakets_b].append(element)
#     elif 'brakets4' in element['mode']:
#         built_formula.append({'mode': 'subformula','tag': '\{\}','value':sub_formula[brakets_b]})
#         brakets_b -= 1
#     elif 'brakets5' in element['mode']:
#         brakets_c += 1
#     elif brakets_c >= 1:
#         sub_formula[brakets_c].append(element)
#     elif 'brakets4' in element['mode']:
#         built_formula.append({'mode': 'subformula','tag': '\[\]','value':sub_formula[brakets_c]})
#         brakets_c -= 1
#     else:
#         built_formula.append(element)