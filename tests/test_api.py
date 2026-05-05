import pytest
from main import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True

    with flask_app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()
    assert data["status"] == "ok"


def test_predict_success(client):
    payload = {
        "LIMIT_BAL": 20000,
        "SEX": 2,
        "EDUCATION": 2,
        "MARRIAGE": 1,
        "AGE": 24,
        "PAY_0": 2,
        "PAY_2": 2,
        "PAY_3": -1,
        "PAY_4": -1,
        "PAY_5": -2,
        "PAY_6": -2,
        "BILL_AMT1": 3913,
        "BILL_AMT2": 3102,
        "BILL_AMT3": 689,
        "BILL_AMT4": 0,
        "BILL_AMT5": 0,
        "BILL_AMT6": 0,
        "PAY_AMT1": 0,
        "PAY_AMT2": 689,
        "PAY_AMT3": 0,
        "PAY_AMT4": 0,
        "PAY_AMT5": 0,
        "PAY_AMT6": 0
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data
    assert "probability" in data
    assert "model_version" in data

    assert data["prediction"] in [0, 1]
    assert 0 <= data["probability"] <= 1


def test_predict_without_json(client):
    response = client.post("/predict")

    assert response.status_code == 400

    data = response.get_json()
    assert "error" in data


def test_predict_missing_features(client):
    payload = {
        "LIMIT_BAL": 20000,
        "SEX": 2
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 400

    data = response.get_json()
    assert "error" in data
    assert "Missing features" in data["error"]