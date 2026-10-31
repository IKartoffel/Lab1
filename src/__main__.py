import argparse
import sys
from . import calculator
from . import convert

def main():
    parser = argparse.ArgumentParser(description="CLI Toolkit")
    subpar = parser.add_subparsers(dest="program", required=True)
    
    # Настройка команд
    calc_parser = subpar.add_parser("calc", help="Калькулятор")
    calc_parser.add_argument("expression", help="Выражение")
    
    conv_parser = subpar.add_parser("conv", help="Конвертер")
    conv_parser.add_argument("value", help="Значение")
    conv_parser.add_argument("unit_from", help="Откуда")
    conv_parser.add_argument("unit_to", help="Куда")
    
    args = parser.parse_args()
    
    try:
        if args.program == "calc":
            result = calculator.calculator_expr(args.expression)
            print(result)
            
        elif args.program == "conv":
            result = convert.convert_explicit(args.value, args.unit_from, args.unit_to)
            print(result)
            
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
