# Ikano Assignment

## Overview

This project implements 3 calculations:

* Fibonacci
* Factorial
* Loan repayment

All calculations are exposed through a REST API built with FastApi. The service includes validation, automated tests, Docker support, CI, and public deployment using Render.

**Live API:**
https://ikano-assignment.onrender.com

**Swagger Documentation:**
https://ikano-assignment.onrender.com/docs

---

## Features

### Fibonacci

**Input:** `n`

**Output:** nth Fibonacci number

**Behaviour:**

* Handles `n = 0` and `n = 1`
* Uses an iterative approach instead of recursive implementation
* Rejects invalid inputs
* Input limited to `500`

### Factorial

**Input:** `n`

**Output:** `n!`

**Behaviour:**

* Handles `0! = 1`
* Rejects negative inputs
* Input limited to `100`
* Large results are returned as strings through the API to avoid JSON precision issues

### Loan Repayment

**Input:** `principal`, `annual_rate`, `months`

**Output:** monthly repayment

**Behaviour:**

* The API accepts `annual_rate` as an annual percentage (for example, `5` means 5% per year)
* The annual rate is converted internally to a monthly rate before applying the repayment formula
* Uses `Decimal` for financial calculations
* Handles zero-interest loans
* Rounds repayments to two decimal places
* Validates invalid inputs

---

## API Endpoints

### Root

```http
GET /
```

Returns basic information about the service and documentation URL.

### Health Check

```http
GET /health
```

Returns service status.

### Fibonacci

```http
POST /fibonacci
```

Example request:

```json
{
  "n": 10
}
```

Example response:

```json
{
  "n": 10,
  "result": "55"
}
```

### Factorial

```http
POST /factorial
```

Example request:

```json
{
  "n": 5
}
```

Example response:

```json
{
  "n": 5,
  "result": "120"
}
```

### Loan Repayment

```http
POST /loan-repayment
```

Example request:

```json
{
  "principal": 100000,
  "annual_rate": 5,
  "months": 360
}
```

Example response:

```json
{
  "principal": "100000",
  "annual_rate": "5",
  "months": 360,
  "monthly_repayment": "536.82"
}
```

---

## Running Locally

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Running Tests

Run the full test suite:

```bash
python -m pytest
```

---

## Docker

Build the image:

```bash
docker build -t ikano-assignment .
```

Run the container:

```bash
docker run -p 8000:8000 ikano-assignment
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## CI

GitHub Actions automatically runs the test suite on pushes to the main branch and on pull requests targeting the main branch.

---

## Deployment

The application is deployed on Render.

**API:**
https://ikano-assignment.onrender.com

**Swagger UI:**
https://ikano-assignment.onrender.com/docs

**Note:** After periods of inactivity, Render free instances may take a few seconds to wake up.

---

## Assumptions

* The `annual_rate` input is treated as an annual percentage rate, not a monthly rate
* Loan repayments use a fixed monthly payment model
* Inputs must be non-negative
* The service is stateless and does not store user data

---

## Limitations

* Fibonacci input is limited to `500`
* Factorial input is limited to `100`
* Loan principal is limited to `1 trillion`
* Loan duration is limited to `1200 months (100 years)`
* Large Fibonacci and factorial results are returned as strings to avoid precision loss and serialization issues in JSON clients

---

## Production Decisions

The assignment was intentionally kept small while applying practical software engineering practices:

* Separation of business logic from API logic
* Input validation using Pydantic models
* Practical input limits for large-number calculations
* Automated unit and API tests
* Health check endpoint
* Structured logging
* Docker packaging
* CI with GitHub Actions
* Public deployment on Render

---

## Future Improvements

Potential future enhancements include:

* Rate limiting
* Metrics and monitoring
* Additional financial calculations
* API versioning