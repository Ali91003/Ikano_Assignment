import pytest
from app.services.factorial import calculate_factorial

def test_factorial_zero():
    assert calculate_factorial(0)==1
def test_factorial_one():
    assert calculate_factorial(1)==1
def test_factorial_normal():
    assert calculate_factorial(5)==120
def test_factorial_negativenumber():
    with pytest.raises(ValueError):
        calculate_factorial(-1)
def test_factorial_noninteger():
    with pytest.raises(ValueError):
        calculate_factorial(3.5)