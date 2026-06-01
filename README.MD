Ikano Assignment

Overview:

This project implements 3 calculations:
- Fibonacci
- Factorial
- Loan repayment

All calculations are exposed through a REST API which was built with FastApi. The service includes validation, automated tests, Docker support, CI, and public deployment using Render.

Live API:
https://ikano-assignment.onrender.com

Swagger Documentation:
https://ikano-assignment.onrender.com/docs

Features:

Fibonacci

Input: n
Output: nth Fibonacci number

Behaviour:
Handles n=0 and n=1
Uses an iterative approach instead of recursive implementation
Rejects invalid inputs
Input limited to 500

Factorial

Input: n
Output: n!

Behaviour:
Handles 0! = 1
Rejects negative inputs
Input limited to 100
Large results are returned as strings through the API to avoid JSON precision issues

Loan Repayment:

Input: principal, annual_rate, months
Output: monthly repayment

Behaviour:
The API accepts annual_rate as an annual percentage, for example 5 means 5% per year. It is converted internally to a monthly rate before applying the loan repayment formula.
Uses Decimal for financial calculations
Handles zero-interest loans
Rounds repayments to two decimal places
Validates invalid inputs

API Endpoints:

Root:

GET /
Returns basic information about the service and documentation URL.

Health Check:

GET /health
Returns service status.

Fibonacci:

POST /fibonacci

Example request:

{
  "n": 10
}

Example response:

{
  "n": 10,
  "result": "55"
}

Factorial
POST /factorial

Example request:

{
  "n": 5
}

Example response:

{
  "n": 5,
  "result": "120"
}

Loan Repayment
POST /loan-repayment

Example request:

{
  "principal": 100000,
  "annual_rate": 5,
  "months": 360
}

Example response:

{
  "principal": "100000",
  "annual_rate": "5",
  "months": 360,
  "monthly_repayment": "536.82"
}

Running locally:

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Start the API:
uvicorn app.main:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

Running Tests

Run the full test suite:
python -m pytest

Docker

Build the image:
docker build -t ikano-assignment .

Run the container:
docker run -p 8000:8000 ikano-assignment

Swagger UI:
http://127.0.0.1:8000/docs

CI

GitHub Actions automatically runs the test suite on pushes to the main branch and on pull requests targeting the main branch.


Deployment

The application is deployed on Render.

API:
https://ikano-assignment.onrender.com

Swagger UI:
https://ikano-assignment.onrender.com/docs

Note: After periods of inactivity, Render free may take a few seconds to wake up.

Assumptions:

The annual_rate input is treated as an annual percentage rate, not a monthly rate.
Loan repayments use a fixed monthly payment model.
Inputs must be non-negative.
The service is stateless and does not store user data.

Limitations:

Fibonacci input is limited to 500.
Factorial input is limited to 100.
Loan principal is limited to 1 trillion.
Loan duration is limited to 1200 months (100 years).
Large Fibonacci and factorial results are returned as strings to avoid precision loss and serialization issues in JSON clients.

Production decisions:

The assignment was intentionally kept small while applying practical SWE practices:

Separation of business logic from API logic
Input validation using Pydantic models
Practical input limits for large-number calculations
Automated unit and API tests
Health check endpoint
Structured logging
Docker packaging
CI with GitHub Actions
Public deployment on Render

Future Improvements

Potential future changes include:

Rate limiting
Metrics and monitoring
Additional financial calculations
API versioning