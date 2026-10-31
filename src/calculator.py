def calculator(s: str):
    s = s.replace(" ","")
    if not expr: # Проверка на пустую строку
        raise ValueError("Тут пусто")
    a = "0123456789+-/*"
    znaki = "+*/"
    for i in range(len(s)): # Поиск неправильных символов
        if s[i] not in a:
            raise ValueError("Символ не из цифр и +-*/, это калькулятор не блокнот")
            f = 1
            break
    for i in range(len(s)): # Поиск деления на ноль
        if s[i] == "/":
            s = s + "1"
            if s[i + 1] == "0" and s[i + 2] == ".":
                s = s[:-1]
            elif s[i + 1] == "0" and s[i + 2] != ".":
                raise ValueError("Делить на ноль нельзя, даже в вузе")
                f = 1
                break
            s = s[:-1]
            
    for i in range(len(s)): # Поиск двойных знаков
        if s[i] == "+" and (s[i + 1] in znaki or s[i + 1] == "-"):
            raise ValueError("Два знака")
        if s[i] == "-" and (s[i + 1] in znaki or s[i + 1] == "-"):
            raise ValueError("Два знака")
        if s[i] == "*" and s[i + 1] in znaki:
            raise ValueError("Два знака")
        if s[i] == "/" and s[i + 1] in znaki:
            raise ValueError("Два знака")
# Счет
if s[0] == '-':
        s = '0' + s
        
    el = ''
    sp = []
    for i in range(len(s)):
        if s[i] in '0123456789.' or (i > 0 and s[i - 1] in "*/" and s[i] == "-"):
            el += s[i]
        else:
            if el != "":
                sp.append(el)
                el = ''
            sp.append(s[i])
    if el != "":
        sp.append(el)

    ch = s.count('*') + s.count('-') + s.count('/') + s.count('+')
    for i in range(ch):
        try:
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
                    sp.pop(sp.index('-')-1)
                    sp.pop(sp.index('-')+1)
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
