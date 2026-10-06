def calculator_expr(s: str) -> float:
    s = s.replace(" ","")
    if s == "": # Проверка на пустую строку
        w = "Тут пусто"
        return w
    a = "0123456789+-/*"
    znaki = "+*/"
    f = 0
    for i in range(len(s)): # Поиск неправильных символов
        if s[i] not in a:
            w = "Символ не из цифр и +-*/, это калькулятор не блокнот"
            return w
            f = 1
            break
    for i in range(len(s)): # Поиск деления на ноль
        if s[i] == "/":
            s = s + "1"
            if s[i + 1] == "0" and s[i + 2] == ".":
                s = s[:-1]
            elif s[i + 1] == "0" and s[i + 2] != ".":
                w = "Делить на ноль нельзя, даже в вузе"
                return w
                f = 1
                break
            
    for i in range(len(s)): # Поиск двойных знаков
        if s[i] == "+" and (s[i + 1] in znaki or s[i + 1] == "-"):
            w = "Два знака"
            return w
            f = 1
            break
        if s[i] == "-" and (s[i + 1] in znaki or s[i + 1] == "-"):
            w = "Два знака"
            return w
            f = 1
            break
        if s[i] == "*" and s[i + 1] in znaki:
            w = "Два знака"
            return w
            f = 1
            break
        if s[i] == "/" and s[i + 1] in znaki:
            w = "Два знака"
            return w
            f = 1
            break
    while f == 0: # Счет 
        if s[0] == '-':
            s = '0' + s
        el = ''
        sp = []
        for i in range(len(s)):
            if s[i] in '0123456789.' or (s[i - 1] in "*/" and s[i] == "-"):
                el += s[i]
            else:
                sp.append(el)
                el = ''
                sp.append(s[i])
        sp.append(el)

        ch = s.count('*') + s.count('-') + s.count('/') + s.count('+')
        for i in range(ch):
            if '*' in sp and '/' in sp:
                if sp.index('*') > sp.index('/'):
                    oper = float(sp[sp.index('/') - 1]) / float(sp[sp.index('/') + 1])
                    sp.pop(sp.index('/')-1)
                    sp.pop(sp.index('/')+1)
                    sp[sp.index('/')] = oper
                        
                else:
                    oper = float(sp[sp.index('*') - 1]) * float(sp[sp.index('*') + 1])
                    sp.pop(sp.index('*')-1)
                    sp.pop(sp.index('*')+1)
                    sp[sp.index('*')] = oper
                        
            elif '*' in sp:
                oper = float(sp[sp.index('*') - 1]) * float(sp[sp.index('*') + 1])
                sp.pop(sp.index('*')-1)
                sp.pop(sp.index('*')+1)
                sp[sp.index('*')] = oper
                    
            elif '/' in sp:
                oper = float(sp[sp.index('/') - 1]) / float(sp[sp.index('/') + 1])
                sp.pop(sp.index('/')-1)
                sp.pop(sp.index('/')+1)
                sp[sp.index('/')] = oper
                    
            elif '+' in sp and '-' in sp:
                if sp.index('+') > sp.index('-'):
                    oper = float(sp[sp.index('-') - 1]) - float(sp[sp.index('-') + 1])
                    sp = sp.pop(sp.index('-')-1)
                    sp = sp.pop(sp.index('-')+1)
                    sp[sp.index('-')] = oper
                        
                else:
                    oper = float(sp[sp.index('+') - 1]) + float(sp[sp.index('+') + 1])
                    sp.pop(sp.index('+')-1)
                    sp.pop(sp.index('+')+1)
                    sp[sp.index('+')] = oper
                        
            elif '+' in sp:
                oper = float(sp[sp.index('+') - 1]) + float(sp[sp.index('+') + 1])
                sp.pop(sp.index('+')-1)
                sp.pop(sp.index('+')+1)
                sp[sp.index('+')] = oper
                    
            elif '-' in sp:
                oper = float(sp[sp.index('-') - 1]) - float(sp[sp.index('-') + 1])
                sp.pop(sp.index('-')-1)
                sp.pop(sp.index('-')+1)
                sp[sp.index('-')] = oper
        return str(sp[0])
        f = 1

def setup_parser(subparsers):
    calc_parser = subparsers.add_parser("calc", help="Калькулятор выражений")
    calc_parser.add_argument("expression", help="Выражение для вычисления")

