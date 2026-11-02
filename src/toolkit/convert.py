from decimal import Decimal, InvalidOperation


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

def convert_explicit(value, from_unit, to_unit):
    try:
        value = Decimal(value)
    except (InvalidOperation, ValueError):
        raise ConversionError("Неверное числовое значение")

    if from_unit not in UNITS or to_unit not in UNITS:
        raise ConversionError("Неизвестная единица измерения")
   
    from_type, from_coef = UNITS[from_unit]
    to_type, to_coef = UNITS[to_unit]

    if from_type != to_type: # Проверка на возможность конвертитровать
        raise ConversionError("Нельзя конвертировать")
 
    if from_type == 'temp':# Провека на абсолютный ноль
        if from_unit == 'c':
            if value < Decimal('-273.15'):
                raise ConversionError("Значение ниже абсолютного нуля")
            base_val = value + Decimal('273.15')
        elif from_unit == 'f':
            if value < Decimal('-459.67'):# Провека на абсолютный ноль
                raise ConversionError("Значение ниже абсолютного нуля")

            base_val = (value - Decimal(32)) * Decimal(5) / Decimal(9) + Decimal('273.15')
        else: 
            if value < Decimal(0):# Провека на абсолютный ноль
                raise ConversionError("Значение ниже абсолютного нуля")

            base_val = value

        if to_unit == 'c':
            result = base_val - Decimal('273.15')
        elif to_unit == 'f':
            result = (base_val - Decimal('273.15')) * Decimal(9) / Decimal(5) + Decimal(32)
        else:
            result = base_val

        return float(result)
            

    base_val = value * from_coef
    result = base_val / to_coef
    return float(result)

