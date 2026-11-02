import pytest

from toolkit.convert import ConversionError, convert_explicit


def test_length():
    assert convert_explicit("1000", "mm", "m") == 1.0

def test_mass():
    assert convert_explicit("1.5", "kg", "g") == 1500.0

def test_temp_c_to_f():
    assert convert_explicit("0", "c", "f") == 32.0

def test_temp_absolute_zero():
    assert convert_explicit("-273.15", "c", "k") == 0.0


def test_below_absolute_zero():
    with pytest.raises(ConversionError, match="ниже абсолютного нуля"):
        convert_explicit("-300", "c", "k")

def test_incompatible_units():
    with pytest.raises(ConversionError, match="Нельзя конвертировать"):
        convert_explicit("1", "kg", "m")

def test_unknown_unit():
    with pytest.raises(ConversionError, match="Неизвестная единица"):
        convert_explicit("1", "parsec", "m")
