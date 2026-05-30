import pytest
from decimal import Decimal
from app.services.loan import calculate_monthly_repayment

def test_with_interest():
    result = calculate_monthly_repayment(
        principal=Decimal("100000"),
        annual_rate=Decimal("5"),
        months=360
    )
    assert result==Decimal("536.82")

def test_zerointerest():
    result = calculate_monthly_repayment(
        principal=Decimal("1200"),
        annual_rate=Decimal("0"),
        months=12
    )
    assert result==Decimal("100.00")

def test_negativeprincipal():
    with pytest.raises(ValueError):
        calculate_monthly_repayment(
            principal=Decimal("-1000"),
            annual_rate=Decimal("5"),
            months=12
        )

def test_negativerate():
    with pytest.raises(ValueError):
        calculate_monthly_repayment(
            principal=Decimal("1000"),
            annual_rate=Decimal("-5"),
            months=12
        )
def test_zeromonths():
    with pytest.raises(ValueError):
        calculate_monthly_repayment(
            principal=Decimal("1000"),
            annual_rate=Decimal("5"),
            months=0
        )

def test_noninteger_months():
    with pytest.raises(ValueError):
        calculate_monthly_repayment(
            principal=Decimal("1000"),
            annual_rate=Decimal("5"),
            months=12.5
        )