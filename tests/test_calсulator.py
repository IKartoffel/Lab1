import pytest
from toolkit.calculator import calculator_expr

def test_priority():
    assert calculator_expr("2 + 3 * 4") == 14.0

def test_float():
    assert calculator_expr("10 / 4") == 2.5

def test_unary_minus():
    assert calculator_expr("2 * -3") == -6.0

def test_spaces():
    assert calculator_expr(" 1 +  2 ") == 3.0

def test_empty_string():
    with pytest.raises(ValueError, match="Пустое выражение"):
        calculator_expr("")

def test_double_operators():
    with pytest.raises(ValueError, match="Два знака"):
        calculator_expr("2*/3")
        
    with pytest.raises(ValueError, match="Два знака"):
        calculator_expr("1 +- 2")

def test_invalid_char():
    with pytest.raises(ValueError, match="Недопустимый символ"):
        calculator_expr("2+a")

def test_division_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль"):
        calculator_expr("1/0")
