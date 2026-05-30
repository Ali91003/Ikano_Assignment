from decimal import Decimal
from pydantic import BaseModel, Field

class NumberInput(BaseModel):
    n: int = Field(..., ge=0, le=10000, description="Non-negative integer")
class FibonacciResponse(BaseModel):
    n: int
    result: int
class FactorialResponse(BaseModel):
    n: int
    result: int
class LoanInput(BaseModel):
    principal: Decimal = Field(..., gt=0, description="Loan amount")
    annual_rate: Decimal = Field(..., ge=0, description="Annual interest rate in percent")
    months: int = Field(..., gt=0, le=1200, description="Loan duration in months")
class LoanResponse(BaseModel):
    principal: Decimal
    annual_rate: Decimal
    months: int
    monthly_repayment: Decimal