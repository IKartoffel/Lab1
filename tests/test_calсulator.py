from toolkit.calculator import calculator_expr


def test_1():
    assert calculator_expr("2 + 3 * 4") == "14.0"

def test_2():
    assert calculator_expr("10 / 4") == "2.5"

def test_3():
   assert calculator_expr("2 * -3") == "-6.0"

def test_4():
    assert calculator_expr("1 +- 2") == "Два знака"

def test_5():
    assert calculator_expr("") == "Тут пусто"

def test_6():
    assert calculator_expr("2*/3") == "Два знака"

def test_7():
    assert calculator_expr("2+a") == "Символ не из цифр и +-*/, это калькулятор не блокнот"

def test_8():
    assert calculator_expr("1/0") == "Делить на ноль нельзя, даже в вузе"
