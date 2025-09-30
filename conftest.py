import pytest
from selenium import webdriver
from config import OPT, PAYMENT_URL, TEST_CARD

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    driver.get(PAYMENT_URL)
    yield driver
    driver.quit()

@pytest.fixture
def test_card():
    return TEST_CARD


# --- Customer Fixtures ---

@pytest.fixture
def customer_factory():
    def _create(**overrides):
        default = {
            "full_name": "ישראל ישראלי",
            "phone": "0501234567",
            "preparation_index": OPT["preparation"]["immediately"],
            "pickles_index": OPT["pickles"]["yes"],
            "chips_index": OPT["chips"]["no"],
            "shipping_index": OPT["shipping"]["pickup"],
            "address": "תל אביב רחוב הרצל 1",
            "notes": "",
            "source_index": OPT["source"]["instagram"]
        }
        default.update(overrides)
        return default
    return _create


@pytest.fixture
def basic_customer(customer_factory):
    return customer_factory()


@pytest.fixture
def delivery_customer(customer_factory):
    return customer_factory(
        full_name="דני כהן",
        phone="0541234567",
        shipping_index=OPT["shipping"]["delivery"],
        address="חיפה רחוב הנשיא 25",
        notes="קומה 3"
    )

@pytest.fixture
def minimal_customer():
    return {
        "full_name": "משה לוי",
        "phone": "0521234567",
        "source_index": OPT["source"]["other"]
    }