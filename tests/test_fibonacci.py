import pytest
from app.services.fibonacci import calculate_fibonacci

def test_fibonacci_zero():
    assert calculate_fibonacci(0)==0
def test_fibonacci_one():
    assert calculate_fibonacci(1)==1
def test_fibonacci_normal():
    assert calculate_fibonacci(10)==55
def test_fibonacci_negativenumber():
    with pytest.raises(ValueError):
        calculate_fibonacci(-1)
def test_fibonacci_noninteger():
    with pytest.raises(ValueError):
        calculate_fibonacci(2.5)