from decimal import Decimal
from pydantic import BaseModel, Field

class FibonacciInput(BaseModel):
    n: int = Field(..., ge=0, le=500, description="Integer between 0 and 500")
class FactorialInput(BaseModel):
    n: int = Field(..., ge=0, le=100, description="Integer between 0 and 100")
class FibonacciResponse(BaseModel):
    n: int
    result: str
class FactorialResponse(BaseModel):
    n: int
    result: str
class LoanInput(BaseModel):
    principal: Decimal = Field(..., gt=0, le=1000000000000, description="Loan amount, maximum 1 trillion")
    annual_rate: Decimal = Field(..., ge=0, le=100, description="Annual interest rate in percent")
    months: int = Field(..., gt=0, le=1200, description="Loan duration in months")
class LoanResponse(BaseModel):
    principal: Decimal
    annual_rate: Decimal
    months: int
    monthly_repayment: Decimal