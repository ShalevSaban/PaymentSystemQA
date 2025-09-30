import requests
import pytest

BASE_URL = "https://sandbox.meshulam.co.il/api/light/server/1.0/createPaymentProcess"

VALID_PAYLOAD = {
    'pageCode': 'e19e0b687744',
    'userId': '52e95954cd5c1311',
    'sum': '100',
    'paymentNum': '1',
    'description': 'ORDER123',
    'pageField[fullName]': 'שם מלא',
    'pageField[phone]': '0534738605',
    'pageField[email]': 'test@example.com'
}


def test_valid_payment_request():
    """Test successful payment creation"""
    response = requests.post(BASE_URL, data=VALID_PAYLOAD)
    data = response.json()

    assert response.status_code == 200
    assert data['status'] == 1
    assert data['err'] == ""
    assert 'processId' in data['data']
    assert 'url' in data['data']


def test_missing_required_field():
    """Test error handling when pageCode is missing"""
    payload = VALID_PAYLOAD.copy()
    del payload['pageCode']

    response = requests.post(BASE_URL, data=payload)
    data = response.json()

    assert data['status'] == "0"
    assert data['err'] != ""


def test_invalid_sum_zero():
    """Test validation for invalid sum value"""
    payload = VALID_PAYLOAD.copy()
    payload['sum'] = '0'

    response = requests.post(BASE_URL, data=payload)
    data = response.json()

    assert data['status'] == "0"
    assert data['err'] != ""

    if isinstance(data['err'], dict):
        assert 'message' in data['err']


def test_invalid_phone_number():
    """Test validation for incomplete phone number"""
    payload = VALID_PAYLOAD.copy()
    payload['pageField[phone]'] = '053'

    response = requests.post(BASE_URL, data=payload)
    data = response.json()

    assert data['status'] == 0
    assert data['err'] != ""
    assert data['err']['id'] == 717


if __name__ == "__main__":
    test_valid_payment_request()
    test_missing_required_field()
    test_invalid_sum_zero()
    print("All tests passed")