# 🧪 QA Project - Grow Company

## 📋 Project Overview
This repository contains automated test solutions for Grow's payment processing system, including UI tests for payment flows and API tests with CI/CD integration.

## 📁 Project Structure
```
├── pages/                      # Page Object Model classes
│   ├── products_page.py       # Product selection page
│   ├── details_page.py        # Customer details form
│   ├── payments_options_page.py  # Payment method selection
│   └── payment_credit_page.py # Credit card payment page
├── tests/
│   ├── test_payment_flow.py   # UI automation tests (Selenium)
│   └── test_api.py            # API tests for payment creation
├── .github/workflows/
│   └── api-tests.yml          # GitHub Actions CI/CD pipeline
├── config.py                  # Test data and configuration
├── conftest.py               # Pytest fixtures
└── requirements.txt          # Python dependencies
```

## ⚙️ Installation & Setup

### ✅ Prerequisites
- Python 3.9+
- Chrome browser
- ChromeDriver (compatible with your Chrome version)

### 📦 Installation Steps
```bash
# Clone the repository
git clone <repository-url>
cd <repository-folder>

# Install dependencies
pip install -r requirements.txt
```

### 📚 Dependencies
- `selenium` - Web automation framework
- `pytest` - Testing framework
- `pytest-html` - HTML test reports
- `requests` - HTTP library for API testing

## 🔧 Configuration

### 🌐 Environment Variables (Optional)
No sensitive credentials required for this sandbox environment. All configuration is in `config.py`:
- `PAYMENT_URL` - Payment page URL
- `TEST_CARD` - Test credit card details
- `PRODUCTS` - Product catalog
- `OPT` - Form options mapping

## 🚀 Running Tests

### 🖥️ UI Tests (Selenium)
```bash
# Run all UI tests
pytest tests/test_payment_flow.py -v

# Run with HTML report
pytest tests/test_payment_flow.py --html=report.html
```

### 🔌 API Tests
```bash
# Run API tests
pytest tests/test_api.py -v

# Run specific test
pytest tests/test_api.py::test_valid_payment_request -v
```

### ✨ All Tests
```bash
pytest -v
```

## 🔄 CI/CD Pipeline

The project includes a GitHub Actions workflow (`.github/workflows/api-tests.yml`) that:
- Triggers on push/PR to main/master branches
- Sets up Python 3.9 environment
- Installs dependencies
- Runs API tests automatically

## ✅ Test Coverage

### 🎯 Critical Features Covered

#### API Tests (`test_api.py`)
1. **Valid payment creation** - Validates successful payment process creation
2. **Missing required fields** - Error handling for missing `pageCode`
3. **Invalid sum validation** - Rejects zero/negative amounts
4. **Phone number validation** - Validates proper phone format

#### UI Tests (`test_payment_flow.py`)
1. **Happy path flow** - Complete purchase journey (product selection → payment → confirmation)
2. **Empty phone field validation** - Verifies required field enforcement and error messages
3. **Invalid credit card** - Tests credit card validation with invalid card number

### 🔍 Coverage Verification Strategy
- **API**: All critical request parameters tested (required fields, validation rules)
- **UI**: End-to-end happy path + critical negative scenarios (form validation, payment errors)
- **Assertions**: Explicit verifications at each critical step
- **Page Objects**: Modular design allows easy test expansion

## 🚀 Future Enhancements

### 🛠️ Recommended Tools & Additions

1. **Allure Reports**
   - Rich visual test reports with screenshots
   - Test history and trends
   - Better failure analysis

2. **Docker**
   - Containerized test environment
   - Consistent execution across machines
   - Easy CI/CD integration


3. **Additional Improvements**
   - Parallel test execution (pytest-xdist)
   - Visual regression testing (Percy/Applitools)
   - Performance testing integration
   - Extended error scenarios coverage
   - Data-driven testing with multiple datasets

## 📐 Page Object Model

The project follows POM design pattern:
- **Separation of concerns**: Test logic separated from page interactions
- **Reusability**: Page methods used across multiple tests
- **Maintainability**: UI changes require updates in one place
- **Readability**: Tests read like user stories

## 📝 Notes
- Tests run against Grow's sandbox environment
- No real transactions are processed
- Test credit card: 4580-4580-4580-4580 (exp: 03/30)
- UI tests can run in headless mode (uncomment in `conftest.py`)



---
✨ **Assignment completed** ✨