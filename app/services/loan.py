from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
def calculate_monthly_repayment(principal: Decimal,annual_rate: Decimal,months: int) -> Decimal:
    try:
        principal =Decimal(principal)
        annual_rate =Decimal(annual_rate)
    except InvalidOperation:
        raise ValueError("principal and annual rate must be valid numbers")
    if principal<=0:
        raise ValueError("principal must be greater than 0")
    if annual_rate<0:
        raise ValueError("annual rate must be greater than or equal to 0")
    if not isinstance(months, int):
        raise ValueError("months must be an integer")
    if months<=0:
        raise ValueError("months must be greater than 0")
    if annual_rate==0:
        monthly_payment =principal/Decimal(months)
    else:
        monthly_rate =annual_rate/Decimal("100")/Decimal("12")
        monthly_payment =principal * (monthly_rate * (Decimal("1") + monthly_rate) ** months)/((Decimal("1") + monthly_rate) ** months - Decimal("1"))

    return monthly_payment.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)