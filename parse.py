def parse_element(element, parsed_elements):
    #brakets
    if '\(' == element:
        parsed_elements.append({'mode': 'brakets1','name': '\('})
    elif '\)' == element:
        parsed_elements.append({'mode': 'brackets2','name': '\)'})
    elif '\{' == element:
        parsed_elements.append({'mode': 'brackets3','name': '\{'})
    elif '\}' == element:
        parsed_elements.append({'mode': 'brackets4','name': '\}'})
    elif '\[' == element:
        parsed_elements.append({'mode': 'brackets5','name': '\['})
    elif '\]' == element:
        parsed_elements.append({'mode': 'brackets6','name': '\]'})                              
    #括弧が必要なやつなど
    elif '\\sqrt' == element:
        parsed_elements.append({'mode': 'sqrt','tag':'msqrt'})  
    elif '\\root' == element:
        parsed_elements.append({'mode': 'root','tag':'mroot'})    
    elif '\\frac' == element:
        parsed_elements.append({'mode': 'frac','tag':'mfrac'})
    elif '\\stackrel' == element:
        parsed_elements.append({'mode': 'stackrel','tag':'mover'})  
    elif '\\atop' == element:
        parsed_elements.append({'mode': 'atop','tag':'mfrac'})    
    elif '\\choose' == element:
        parsed_elements.append({'mode': 'choose','tag':'mfrac'})
    elif '_' == element:                                 
        parsed_elements.append({'mode': 'sub','tag':'msub','name': '_'})
    elif '\^' == element:
        parsed_elements.append({'mode': 'sup','tag':'msup','name': '^'})  
    elif '\\mathrm' == element:
        parsed_elements.append({'mode': 'text','tag':'text','name': '\)'})    
    elif '\\mbox' == element:
        parsed_elements.append({'mode': 'mbox','tag':'mbox','name': '\)'})
    #関数
    elif '\\arccos' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'arccos'})
    elif '\\arcsin' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'arcsin'})
    elif '\\arctan' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'arctan'})
    elif '\\arg' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'arg'})
    elif '\\cos' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'cos'})
    elif '\\csh' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'csh'})
    elif '\\cot' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'cot'})
    elif '\\coth' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'coth'})
    elif '\\csc' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'csc'})
    elif '\\deg' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'deg'})
    elif '\\det' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'det'})
    elif '\\dim' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'dim'})
    elif '\\exp' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'exp'})
    elif '\\gcd' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'gcd'})
    elif '\\hom' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'hom'})
    elif '\\inf' == element:
        parsed_elements.append({'mode': 'function','tag':'mo','name': 'inf', 'type': 'underover'})
    elif '\\ker' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'ker'})
    elif '\\lg' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'lg'})            
    elif '\\lim' == element:
        parsed_elements.append({'mode': 'function','tag':'mo','name': 'lim','type':'underover'})
    elif '\\liminf' == element:
        parsed_elements.append({'mode': 'function','tag':'mo','name': 'liminf','type':'underover'})
    elif '\\limsup' == element:
        parsed_elements.append({'mode': 'function','name': 'limsup','type':'underover'})
    elif '\\ln' == element:
        parsed_elements.append({'mode': 'function','name': 'ln'})
    elif '\\log' == element:
        parsed_elements.append({'mode': 'function','name': 'log'})
    elif '\\max' == element:
        parsed_elements.append({'mode': 'function','tag':'mo','name': 'max','type':'underover'})
    elif '\\min' == element:
        parsed_elements.append({'mode': 'function','tag':'mo','name': 'min','type':'underover'})
    elif '\\Pr' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'Pr'})
    elif '\\sec' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'sec'})
    elif '\\sin' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'sin'})
    elif '\\sinh' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'sinh'})
    elif '\\sup' == element:
        parsed_elements.append({'mode': 'function','tag':'mo','name': 'sup','type':'undercover'})
    elif '\\tan' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'tan'})
    elif '\\tanh' == element:
        parsed_elements.append({'mode': 'function','tag':'mi','name': 'tanh'})                                 
    #演算子2
    elif '+' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '+'})
    elif '-' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '-'})
    elif '\\pm' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\PlusMinus;'})           
    elif '\\mp' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2213'})
    elif '\\triangleleft' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B2'})
    elif '\\triangleright' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B3'})
    elif '\\cdot' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22C5'})
    elif '\\star' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22C6'})
    elif '\\ast' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u002A'})
    elif '\\times' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u00D7'})
    elif '\\div' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u00F7'})
    elif '\\circ' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2218'})
    elif '\\bullet' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2022'})
    elif '\\oplus' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2295'})
    elif '\\ominus' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2296'})
    elif '\\otimes' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2297'})
    elif '\\bigcirc' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u25CB'})
    elif '\\oslash' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2298'})
    elif '\\odot' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2299'})
    elif '\\land' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2227'})
    elif '\\wedge' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2227'})
    elif '\\lor' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2228'})
    elif '\\vee' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2228'})        
    elif '\\cap' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2229'})
    elif '\\cup' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u222A'})
    elif '\\spcap' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2293'})
    elif '\\spcup' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2294'})
    elif '\\uplus' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u228E'})
    elif '\\amalg' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2210'})
    elif '\\bigtriangleup' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u25B3'})      
    elif '\\bigtriangledown' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u25BD'})
    elif '\\dag' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2020'})
    elif '\\dagger' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2020'})
    elif '\\ddag' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2021'})
    elif '\\ddagger' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u2021'})
    elif '\\lhd' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B2'})
    elif '\\rhd' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B3'})
    elif '\\unlhd' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B4'})
    elif '\\unrhd' == element:
        parsed_elements.append({'mode': 'operator2','tag':'mo','name': '\u22B5'})
    #演算子3
    elif '\\sum' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u2211','type':'underover'})
    elif '\\prod' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u220F','type':'underover'})
    elif '\\bigcap' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u22C2','type':'underover'})
    elif '\\bigwedge' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u22C3','type':'underover'})
    elif '\\bigvee' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u22C0','type':'underover'})
    elif '\\bigsqcap' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u22C1','type':'underover'})
    elif '\\bigsqcup' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u2A05','type':'underover'})
    elif '\\coprod' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u2A06','type':'underover'})
    elif '\\bigoplus' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u2A01','type':'underover'})
    elif '\\bigotimes' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u2A02','type':'underover'})
    elif '\\bigodot' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u2A00','type':'underover'})
    elif '\\biguplus' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u2A04','type':'underover'})      
    elif '\\int' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u222B'})
    elif '\\oint' == element:
        parsed_elements.append({'mode': 'operator3','tag':'mo','name': '\u222E'})
    #二項関係記号
    elif '=' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '='})
    elif ':=' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': ':='})
    elif '\\lt' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '<'})
    elif '\\gt' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '>'})
    elif '\\ne' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2260'})
    elif '\\neq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2260'})      
    elif '\\le' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2264'})
    elif '\\leq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2264'})
    elif '\\leqslant' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2264'})
    elif '\\ge' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2265'})      
    elif '\\geq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2265'})
    elif '\\geqslant' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2265'})
    elif '\\equiv' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2261'})
    elif '\\ll' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u226A'})
    elif '\\gg' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u226B'})
    elif '\\doteq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2250'})      
    elif '\\preq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u227A'})
    elif '\\succ' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u227B'})
    elif '\\preceq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u227C'})
    elif '\\succeq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u227D'})
    elif '\\subset' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2282'})
    elif '\\supset' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2283'})
    elif '\\subseteq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2286'})
    elif '\\supseteq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2287'})
    elif '\\sqsubset' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u228F'})      
    elif '\\sqsupset' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2290'})
    elif '\\sqsubseteq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2291'})
    elif '\\sqsupseteq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2292'})
    elif '\\sim' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u223C'})      
    elif '\\simeq' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2243'})
    elif '\\approx' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2248'})
    elif '\\cong' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2245'})
    elif '\\Join' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22C8'})
    elif '\\bowtie' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2208'})
    elif '\\in' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u220B'})      
    elif '\\ni' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u220B'})
    elif '\\owns' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u221D'})
    elif '\\propto' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22A2'})
    elif '\\vdash' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22A3'})
    elif '\\models' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22A8'})
    elif '\\perp' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u22A5'})
    elif '\\smile' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2323'})
    elif '\\frown' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2322'})
    elif '\\asymp' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u224D'})      
    elif '\\notin' == element:
        parsed_elements.append({'mode': 'symbol','tag':'mo','name': '\u2209'})
    #特殊文字
    elif '\\alpha' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B1'})
    elif '\\beta' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B2'})
    elif '\\gamma' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B3'})      
    elif '\\delta' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B4'})
    elif '\\epsilon' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B5'})
    elif '\\varepsilon' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u025B'})
    elif '\\zeta' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B6'})
    elif '\\eta' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B7'})
    elif '\\theta' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B8'})      
    elif '\\vartheta' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03D1'})
    elif '\\iota' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03B9'})
    elif '\\kappa' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03BA'})
    elif '\\lambda' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03BB'})
    elif '\\mu' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03BC'})
    elif '\\nu' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03BD'})
    elif '\\xi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03BE'})      
    elif '\\pi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C0'})
    elif '\\varpi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03D6'})
    elif '\\rho' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C1'})
    elif '\\varrho' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03F1'})
    elif '\\varsigma' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C2'})
    elif '\\sigma' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C3'})      
    elif '\\tau' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C4'})
    elif '\\upsilon' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C5'})
    elif '\\phi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C6'})
    elif '\\varphi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03D5'})
    elif '\\chi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C7'})
    elif '\\psi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C8'})
    elif '\\omega' == element:
        parsed_elements.append({'mode': 'greek','tag':'mi','name': '\u03C9'})      
    elif '\\Gamma' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u0393'})
    elif '\\Delta' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u0394'})
    elif '\\Theta' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u0398'})
    elif '\\Lambda' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u039B'})
    elif '\\Xi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u039E'})
    elif '\\Pi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u03A0'})      
    elif '\\Sigma' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u03A3'})
    elif '\\Upsilon' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u03A5'})
    elif '\\Phi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u03A6'})
    elif '\\Psi' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u03A8'})
    elif '\\Omega' == element:
        parsed_elements.append({'mode': 'greek','tag':'mo','name': '\u03A9'})
    #分数
    elif '\\frac12' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u00BD'})
    elif '\\frac14' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u00BC'})
    elif '\\frac34' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u00BE'})
    elif '\\frac13' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2153'})
    elif '\\frac23' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2154'})
    elif '\\frac15' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2155'})
    elif '\\frac25' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2156'})
    elif '\\frac35' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2157'})
    elif '\\frac45' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2158'})
    elif '\\frac16' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u2159'})
    elif '\\frac56' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215A'})
    elif '\\frac18' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215B'})
    elif '\\frac38' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215C'})
    elif '\\frac58' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215D'})
    elif '\\frac78' == element:
        parsed_elements.append({'mode': 'frac','tag':'mo','name': '\u215E'})
    #矢印
    elif '\\gets' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2910'})
    elif '\\leftarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2190'})
    elif '\\to' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2192'})            
    elif '\\rightarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2192'})
    elif '\\leftrightarrows' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2194'})
    elif '\\uparrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2191'})            
    elif '\\downarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2193'})
    elif '\\updownarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2195'})
    elif '\\Leftarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D0'})            
    elif '\\Rightarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D2'})
    elif '\\Leftrightarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D4'})
    elif '\\Uparrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D1'})            
    elif '\\Downarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D3'})
    elif '\\mapsto' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D5'})
    elif '\\longleftarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21A6'})            
    elif '\\longrightarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2190'})
    elif '\\longleftrightarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u2192'})
    elif '\\Longleftarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D0'})            
    elif '\\Longrightarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D2'})
    elif '\\Longleftrightarrow' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21D4'})
    elif '\\Longmapsto' == element:
        parsed_elements.append({'mode': 'arrows','tag':'mo','name': '\u21A6'})            
    
    #英数字
    elif str.isdigit(element):
        parsed_elements.append({'mode': 'number','value': element})
    else:
        parsed_elements.append({'mode': 'characters','value': element})