import pytest
from betterCalculator import BetterCalculator

def test_Add():
    assert(BetterCalculator.Add(5, 3) == 8)

def test_Minus():
    assert(BetterCalculator.Minus(5, 3) == 2)

def test_Multiple():
    assert(BetterCalculator.Multiple(5, 3) == 15)

def test_Divide():
    assert(BetterCalculator.Divide(15, 3) == 5)
    
def test_Mod():
    assert(BetterCalculator.Mod(5, 3) == 2)

def test_Conj():
    assert(BetterCalculator.Conj(5, 3) == "53")

def test_Pow():
    assert(BetterCalculator.Pow(5, 3) == 125)
