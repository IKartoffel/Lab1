from toolkit.convert import convert_explicit
from decimal import Decimal
import pytest

def test_1():
    assert convert_explicit("1000", "mm", "m") == "1.0 m"

def test_2():
    assert convert_explicit("1.5", "kg", "g") == "1500.0 g"

def test_3():
    assert convert_explicit("0", "c", "f") == "32.0 f"

def test_4():
    assert convert_explicit("-273.15", "c", "k") == "0.0 k"

