import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()


def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200


def test_prediction(client):
    test_data ={"ApplicantIncome": 500000,
                "Credit_History": 0.0,
                "Gender": "Male",
                "LoanAmount": 200000,
                "Married": "Unmarried"}

    resp = client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.json == {'Loan Approval Status': 'Rejection'}