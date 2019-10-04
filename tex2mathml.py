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
        #演算子1
        if '\(' in elements:
            parsed_elements.append({'mode': 'operator1','name': '\('})
        elif '\)' in elements:
            parsed_elements.append({'mode': 'operator1','name': '\)'})
        #関数
        elif '\\arccos' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'arccos'})
        elif '\\arcsin' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'arcsin'})
        elif '\\arctan' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'arctan'})
        elif '\\arg' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'arg'})
        elif '\\cos' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'cos'})
        elif '\\csh' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'csh'})
        elif '\\cot' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'cot'})
        elif '\\coth' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'coth'})
        elif '\\csc' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'csc'})
        elif '\\deg' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'deg'})
        elif '\\det' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'det'})
        elif '\\dim' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'dim'})
        elif '\\exp' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'exp'})
        elif '\\gcd' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'gcd'})
        elif '\\hom' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'hom'})
        elif '\\inf' in elements:
            parsed_elements.append({'mode': 'function','tag':'mo','name': 'inf', 'type': 'underover'})
        elif '\\ker' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'ker'})
        elif '\\lg' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'lg'})            
        elif '\\lim' in elements:
            parsed_elements.append({'mode': 'function','tag':'mo','name': 'lim','type':'underover'})
        elif '\\liminf' in elements:
            parsed_elements.append({'mode': 'function','tag':'mo','name': 'liminf','type':'underover'})
        elif '\\limsup' in elements:
            parsed_elements.append({'mode': 'function','name': 'limsup','type':'underover'})
        elif '\\ln' in elements:
            parsed_elements.append({'mode': 'function','name': 'ln'})
        elif '\\log' in elements:
            parsed_elements.append({'mode': 'function','name': 'log'})
        elif '\\max' in elements:
            parsed_elements.append({'mode': 'function','tag':'mo','name': 'max','type':'underover'})
        elif '\\min' in elements:
            parsed_elements.append({'mode': 'function','tag':'mo','name': 'min','type':'underover'})
        elif '\\Pr' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'Pr'})
        elif '\\sec' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'sec'})
        elif '\\sin' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'sin'})
        elif '\\sinh' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'sinh'})
        elif '\\sup' in elements:
            parsed_elements.append({'mode': 'function','tag':'mo','name': 'sup','type':'undercover'})
        elif '\\tan' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'tan'})
        elif '\\tanh' in elements:
            parsed_elements.append({'mode': 'function','tag':'mi','name': 'tanh'})                                 
        #演算子2
        elif '\+' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\+'})
        elif '-' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '-'})
        elif '\\pm' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\PlusMinus;'})           
        elif '\\mp' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2213'})
        elif '\\triangleleft' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B2'})
        elif '\\triangleright' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B3'})
        elif '\\cdot' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22C5'})
        elif '\\star' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22C6'})
        elif '\\ast' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u002A'})
        elif '\\times' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u00D7'})
        elif '\\div' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u00F7'})
        elif '\\circ' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2218'})
        elif '\\bullet' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2022'})
        elif '\\oplus' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2295'})
        elif '\\ominus' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2296'})
        elif '\\otimes' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2297'})
        elif '\\bigcirc' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u25CB'})
        elif '\\oslash' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2298'})
        elif '\\odot' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2299'})
        elif '\\land' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2227'})
        elif '\\wedge' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2227'})
        elif '\\lor' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2228'})
        elif '\\vee' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2228'})        
        elif '\\cap' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2229'})
        elif '\\cup' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u222A'})
        elif '\\spcap' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2293'})
        elif '\\spcup' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2294'})
        elif '\\uplus' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u228E'})
        elif '\\amalg' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2210'})
        elif '\\bigtriangleup' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u25B3'})      
        elif '\\bigtriangledown' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u25BD'})
        elif '\\dag' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2020'})
        elif '\\dagger' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2020'})
        elif '\\ddag' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2021'})
        elif '\\ddagger' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2021'})
        elif '\\lhd' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B2'})
        elif '\\rhd' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B3'})
        elif '\\unlhd' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B4'})
        elif '\\unrhd' in elements:
            parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B5'})
        #演算子3
        elif '\\sum' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\prod' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\bigcap' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\bigwedge' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\bigvee' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\bigsqcap' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\bigsqcup' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\coprod' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\bigoplus' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\bigotimes' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\bigodot' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\biguplus' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})      
        elif '\\int' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        elif '\\oint' in elements:
            parsed_elements.append({'mode': 'operator3','tag':'mo','name': '','type':'underover'})
        #二項関係記号
        elif '=' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '='})
        elif ':=' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': ':='})
        elif '\\lt' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '<'})
        elif '\\gt' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '>'})
        elif '\\ne' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2260'})
        elif '\\neq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2260'})      
        elif '\\le' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2264'})
        elif '\\leq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2264'})
        elif '\\leqslant' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2264'})
        elif '\\ge' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2265'})      
        elif '\\geq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2265'})
        elif '\\geqslant' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2265'})
        elif '\\equiv' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2261'})
        elif '\\ll' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u226A'})
        elif '\\gg' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u226B'})
        elif '\\doteq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2250'})      
        elif '\\preq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u227A'})
        elif '\\succ' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u227B'})
        elif '\\preceq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u227C'})
        elif '\\succeq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u227D'})
        elif '\\subset' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2282'})
        elif '\\supset' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2283'})
        elif '\\subseteq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2286'})
        elif '\\supseteq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2287'})
        elif '\\sqsubset' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u228F'})      
        elif '\\sqsupset' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2290'})
        elif '\\sqsubseteq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2291'})
        elif '\\sqsupseteq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2292'})
        elif '\\sim' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u223C'})      
        elif '\\simeq' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2243'})
        elif '\\approx' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2248'})
        elif '\\cong' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2245'})
        elif '\\Join' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22C8'})
        elif '\\bowtie' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2208'})
        elif '\\in' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u220B'})      
        elif '\\ni' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u220B'})
        elif '\\owns' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u221D'})
        elif '\\propto' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22A2'})
        elif '\\vdash' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22A3'})
        elif '\\models' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22A8'})
        elif '\\perp' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22A5'})
        elif '\\smile' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2323'})
        elif '\\frown' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2322'})
        elif '\\asymp' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u224D'})      
        elif '\\notin' in elements:
            parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2209'})
        #特殊文字
        elif '\\alpha' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B1'})
        elif '\\beta' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B2'})
        elif '\\gamma' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B3'})      
        elif '\\delta' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B4'})
        elif '\\epsilon' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B5'})
        elif '\\varepsilon' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u025B'})
        elif '\\zeta' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B6'})
        elif '\\eta' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B7'})
        elif '\\theta' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B8'})      
        elif '\\vartheta' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03D1'})
        elif '\\iota'' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03B9'})
        elif '\\kappa' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03BA'})
        elif '\\lambda' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03BB'})
        elif '\\mu' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03BC'})
        elif '\\nu' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03BD'})
        elif '\\xi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03BE'})      
        elif '\\pi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C0'})
        elif '\\varpi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03D6'})
        elif '\\rho' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C1'})
        elif '\\varrho' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03F1'})
        elif '\\varsigma' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C2'})
        elif '\\sigma' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C3'})      
        elif '\\tau' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C4'})
        elif '\\upsilon' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C5'})
        elif '\\phi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C6'})
        elif '\\varphi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03D5'})
        elif '\\chi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C7'})
        elif '\\psi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C8'})
        elif '\\omega' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mi','name': '\u03C9'})      
        elif '\\Gamma' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u0393'})
        elif '\\Delta' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u0394'})
        elif '\\Theta' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u0398'})
        elif '\\Lambda' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u039B'})
        elif '\\Xi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u039E'})
        elif '\\Pi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u03A0'})      
        elif '\\Sigma' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u03A3'})
        elif '\\Upsilon' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u03A5'})
        elif '\\Phi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u03A6'})
        elif '\\Psi' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u03A8'})
        elif '\\Omega' in elements:
            parsed_elements.append({'mode': 'characters','tag':'mo','name': '\u03A9'})
        #分数
        elif '\\frac12' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u00BD'})
        elif '\\frac14' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u00BC'})
        elif '\\frac34' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u00BE'})
        elif '\\frac13' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2153'})
        elif '\\frac23' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2154'})
        elif '\\frac15' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2155'})
        elif '\\frac25' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2156'})
        elif '\\frac35' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2157'})
        elif '\\frac45' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2158'})
        elif '\\frac16' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2159'})
        elif '\\frac56' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215A'})
        elif '\\frac18' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215B'})
        elif '\\frac38' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215C'})
        elif '\\frac58' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215D'})
        elif '\\frac78' in elements:        elif '\\frac25' in elements:
            parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215E'})
        #英数字
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
    elif 
        if 'operator2' in formulas.get('mode'):　#演算子
            operator = et.SubElement(math,'mo')
            operator.text = formulas.get('name')
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