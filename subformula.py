#箱に入れていく関数
def makebox():
    box = []
    if 
        box.append({'mode': 'subformula','tag': 'mrow','value':box})
    elif 
        makebox()

def makesubformula(element, built_formula,sub_formula,brakets_a,brakets_b,brakets_c):
    if 'brakets1' in element['mode']:
        brakets_a += 1
    elif brakets_a >= 1:
        sub_formula[brakets_a].append(element)
    elif 'brakets2' in element['mode']:
        if brakets_a == 0:
            built_formula.append({'mode': 'subformula','tag': 'mrow','value':sub_formula[brakets_a]})
        brakets_a -= 1
    elif 'brakets3' in element['mode']:
        brakets_b += 1
    elif brakets_b >= 1:
        sub_formula[brakets_b].append(element)
    elif 'brakets4' in element['mode']:
        built_formula.append({'mode': 'subformula','tag': '\{\}','value':sub_formula[brakets_b]})
        brakets_b -= 1
    elif 'brakets5' in element['mode']:
        brakets_c += 1
    elif brakets_c >= 1:
        sub_formula[brakets_c].append(element)
    elif 'brakets4' in element['mode']:
        built_formula.append({'mode': 'subformula','tag': '\[\]','value':sub_formula[brakets_c]})
        brakets_c -= 1
    else:
        built_formula.append(element)