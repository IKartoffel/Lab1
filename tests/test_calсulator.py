import pytest

from toolkit.calculator import calculator


def test_priority():
    assert calculator("2 + 3 * 4") == 14.0

def test_float():
    assert calculator("10 / 4") == 2.5

def test_unary_minus():
    assert calculator("2 * -3") == -6.0

def test_spaces():
    assert calculator(" 1 +  2 ") == 3.0

def test_empty_string():
    with pytest.raises(ValueError, match="Тут пусто"):
        calculator("")

def test_double_operators():
    with pytest.raises(ValueError, match="Два знака"):
        calculator("2*/3")
        
    with pytest.raises(ValueError, match="Два знака"):
        calculator("1 +- 2")

def test_invalid_char():
    with pytest.raises(ValueError, match="Символ не из цифр"):
        calculator("2+a")

def test_division_by_zero():
    with pytest.raises(ValueError, match="Делить на ноль нельзя, даже в вузе"):
        calculator("1/0")
