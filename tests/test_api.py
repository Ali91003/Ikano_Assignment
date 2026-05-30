from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)
def test_health_check():
    response = client.get("/health")

    assert response.status_code==200
    assert response.json()=={
        "status": "healthy",
        "service": "ikano-assignment",
        "version": "1.0.0",
    }

def test_fibonacci():
    response = client.post("/fibonacci", json={"n": 10})
    assert response.status_code==200
    assert response.json()=={"n": 10, "result": 55}

def test_factorial():
    response = client.post("/factorial", json={"n": 5})
    assert response.status_code==200
    assert response.json()=={"n": 5, "result": 120}

def test_loan_repayment():
    response = client.post(
        "/loan-repayment",
        json={
            "principal": 100000,
            "annual_rate": 5,
            "months": 360
        },
    )
    assert response.status_code==200
    assert response.json()=={
        "principal": "100000",
        "annual_rate": "5",
        "months": 360,
        "monthly_repayment": "536.82"
    }

def test_fibonacci_negativenumber():
    response = client.post("/fibonacci", json={"n": -1})
    assert response.status_code==422

def test_factorial_negativenumber():
    response = client.post("/factorial", json={"n": -1})
    assert response.status_code==422

def test_loan_repayment_invalidmonths():
    response = client.post(
        "/loan-repayment",
        json={
            "principal": 100000,
            "annual_rate": 5,
            "months": 0
        },
    )
    assert response.status_code==422

def test_fibonacci_toolargenumber():
    response = client.post("/fibonacci", json={"n": 10001})
    assert response.status_code==422

def test_loan_repayment_toomanymonths():
    response = client.post(
        "/loan-repayment",
        json={
            "principal": 100000,
            "annual_rate": 5,
            "months": 1201,
        },
    )
    assert response.status_code==422