import argparse
import sys

import calculator
import convert


def main():
    parser = argparse.ArgumentParser(description="CLI Toolkit")
    subpar = parser.add_subparsers(dest="program", required=True)
    calculator.setup_parser(subpar)
    convert.setup_parser(subpar)
    args = parser.parse_args()
    if args.program == "calc":
        result = calculator.calculator_expr(args.expression)
        sys.stdout.write(str(result))
    elif args.program == "conv":
        result = convert.convert_explicit(args.value, args.unit_from, args.unit_to)
        sys.stdout.write(str(result))


if __name__ == "__main__":
    main()
