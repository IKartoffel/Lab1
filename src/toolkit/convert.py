from decimal import Decimal


class ConversionError(Exception):
    pass
"""
Создание словаря для удобного счета
"""
UNITS = {
    'm': ('length', Decimal(1)),
    'mm': ('length', Decimal('0.001')),
    'cm': ('length', Decimal('0.01')),
    'km': ('length', Decimal(1000)),
    'kg': ('mass', Decimal(1)),
    'g': ('mass', Decimal('0.001')),
    't': ('mass', Decimal(1000)),
    'k': ('temp', None),
    'c': ('temp', None),
    'f': ('temp', None),
}

def convert_explicit(value_str, from_unit, to_unit):
    """
    Разделение на разные переменные
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    value = Decimal(value_str)
    for i in str(value_str):#Поиск неправильного символа в числе
        if i not in "0123456789-.":
            w = "Символ не из цифр и не -, это конвертер не блокнот"
            return w
            break
        
    if from_unit not in UNITS or to_unit not in UNITS:# Поиск неправильного символа в единицах измерения
        w = "Неизвестная единица измерения"
        return w
   
    from_type, from_coef = UNITS[from_unit]
    to_type, to_coef = UNITS[to_unit]

    if from_type != to_type: # Проверка на возможность конвертитровать
        w = "Нельзя конвертировать"
        return w
 
    if from_type == 'temp':# Провека на абсолютный ноль
        if from_unit == 'c':
            if value < Decimal('-273.15'):
                w = "Значение ниже абсолютного нуля"
                return w

            base_val = value + Decimal('273.15')
        elif from_unit == 'f':
            if value < Decimal('-459.67'):# Провека на абсолютный ноль
                w = "Значение ниже абсолютного нуля"
                return w

            base_val = (value - Decimal(32)) * Decimal(5) / Decimal(9) + Decimal('273.15')
        else: 
            if value < Decimal(0):# Провека на абсолютный ноль
                w = "Значение ниже абсолютного нуля"
                return w

            base_val = value

        if to_unit == 'c':
            result = base_val - Decimal('273.15')
        elif to_unit == 'f':
            result = (base_val - Decimal('273.15')) * Decimal(9) / Decimal(5) + Decimal(32)
        else:
            result = base_val
            
        return f'{float(result)} {to_unit}'

    base_val = value * from_coef
    result = base_val / to_coef
    return f'{float(result)} {to_unit}'


def setup_parser(subparsers):
    conv_parser = subparsers.add_parser("conv", help="Конвертер единиц")
    conv_parser.add_argument("value", type=float, help="Значение для конвертации")
    conv_parser.add_argument("unit_from", help="Единица измерения исходного значения")
    conv_parser.add_argument("unit_to", help="Единица измерения целевого значения")
