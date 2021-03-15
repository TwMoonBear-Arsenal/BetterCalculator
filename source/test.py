import pytest
from betterCalculator import BetterCalculator


def test_AlwaysTrue():
    assert 1 == 1


def test_Mod():
    assert(BetterCalculator.Mod(5, 3) == 2)


def test_Conj():
    assert(BetterCalculator.Conj(5, 3) == "53")


def test_Gcd():
    assert(BetterCalculator.Gcd(15, 9) == 3)


def test_Pow():
    assert(BetterCalculator.Pow(5, 3) == 125)
