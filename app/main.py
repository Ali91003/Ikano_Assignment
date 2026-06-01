from fastapi import FastAPI, HTTPException

from app.logger import logger
from app.schemas import (
    FibonacciInput,
    FactorialInput,
    FibonacciResponse,
    FactorialResponse,
    LoanInput,
    LoanResponse,
)
from app.services.fibonacci import calculate_fibonacci
from app.services.factorial import calculate_factorial
from app.services.loan import calculate_monthly_repayment

app = FastAPI(
    title="Ikano Assignment",
    description="Assignment which has Fibonacci, factorial, and loan repayment calculations.",
    version="1.0.0",
)
@app.get("/")
def root():
    return {
        "message": "Ikano Assignment is running",
        "docs": "/docs",
        "health": "/health",
    }
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ikano-assignment",
        "version": "1.0.0",
    }

@app.post("/fibonacci", response_model=FibonacciResponse)
def fibonacci(input_data: FibonacciInput):
    try:
        logger.info(f"Fibonacci request received: n={input_data.n}")
        result = calculate_fibonacci(input_data.n)
        return FibonacciResponse(n=input_data.n, result=str(result))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@app.post("/factorial", response_model=FactorialResponse)
def factorial(input_data: FactorialInput):
    try:
        logger.info(f"Factorial request received: n={input_data.n}")
        result = calculate_factorial(input_data.n)
        return FactorialResponse(n=input_data.n, result=str(result))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

@app.post("/loan-repayment", response_model=LoanResponse)
def loan_repayment(input_data: LoanInput):
    try:
        logger.info(
            f"Loan repayment request received: principal={input_data.principal}, "
            f"annual_rate={input_data.annual_rate}, months={input_data.months}"
        )
        monthly_repayment = calculate_monthly_repayment(
            principal=input_data.principal,
            annual_rate=input_data.annual_rate,
            months=input_data.months,
        )
        return LoanResponse(
            principal=input_data.principal,
            annual_rate=input_data.annual_rate,
            months=input_data.months,
            monthly_repayment=monthly_repayment,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))