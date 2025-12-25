# Playwright_Assignment

A comprehensive Playwright automation framework for testing the TodoMVC application. This project demonstrates a robust, maintainable test framework with cross-browser testing capabilities, detailed reporting, and parallel execution.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Test Reports](#test-reports)
- [Framework Features](#framework-features)

---

## 🎯 Project Overview

This framework is designed to:
- **Test TodoMVC Application** with comprehensive test coverage
- **Support Multiple Browsers** (Chromium, Firefox)
- **Run Tests in Parallel** for faster execution
- **Generate Detailed Reports** using Allure and HTML reports
- **Follow Page Object Model (POM)** design pattern for maintainability
- **Capture Screenshots** for all tests automatically

**Test Application URL:** https://demo.playwright.dev/todomvc/#/

---

## 📦 Prerequisites

Before setting up the project, ensure you have:

- **Python:** 3.8 or higher ([Download Python](https://www.python.org/downloads/))
- **pip:** Python package manager (comes with Python)
- **Git:** For version control
- **Windows/Mac/Linux:** This framework supports all operating systems

To verify your Python installation, run:
```
python --version
pip --version
```

## 🚀 Installation

Follow these steps to set up the project:

### Step 1: Clone the Repository
```
git clone <repository-url>
cd Playwright_Assignment
```

### Step 2: Create a Virtual Environment (Recommended)
```
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```
pip install -r requirements.txt
```

### Step 4: Install Playwright Browsers
After installing the requirements, install the required browsers:
```
playwright install
```

## 📁 Project Structure

```
Playwright_Assignment/
├── conftest.py                 # Pytest configuration and fixtures
├── pytest.ini                  # Pytest configuration file
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── config/                     # Configuration files
├── pages/                      # Page Object Models
│   ├── __init__.py
│   ├── BasePage.py            # Base page class with common methods
│   └── TodoPage.py            # TodoMVC page object
├── tests/                      # Test files
│   ├── __init__.py
│   ├── test_ui_validation.py   # UI validation tests
│   ├── test_filter_tabs.py     # Filter tab tests
│   └── test_todo_functionality.py # Functionality tests
├── utils/                      # Utility modules
│   ├── __init__.py
│   └── data_reader.py          # Data reading utilities
├── testdata/                   # Test data files
│   └── data.json              # Test data
├── reports/                    # Test reports
│   ├── assignment.html        # HTML report
│   ├── allure-report/         # Allure HTML report
│   ├── allure-results/        # Allure test results
│   └── screenshots/           # Test screenshots
└── test-results/              # Playwright test results
```

## ⚙️ Configuration

### pytest.ini Configuration

The `pytest.ini` file contains important test configurations:

```ini
[pytest]
addopts =
    --browser=chromium
    --browser=firefox
    --headed
    --base-url=https://demo.playwright.dev/todomvc/#/
    --screenshot=on
    --tracing=on
    --html=reports/assignment.html --capture=tee-sys
    --alluredir=reports/allure-results
    -n 2
```

**Key Configuration Options:**

 `--browser=chromium` --- Run tests on Chromium browser 
 `--browser=firefox` --- Run tests on Firefox browser 
 `--headed` --- Run tests in headed mode (visible browser) 
 `--base-url` --- Base URL for the TodoMVC application 
 `--screenshot=on` --- Enable automatic screenshots 
 `--tracing=on` --- Enable trace recording for debugging 
 `--html=reports/` --- Generate HTML report 
 `--alluredir=` --- Directory for Allure results 
 `-n 2` --- Run 2 parallel workers 

---

## 🧪 Running Tests

### Step 1: Basic Test Run
Run all tests with default configuration:
```bash
pytest
```

### Step 2: Run Tests on Specific Browser
Run
pytest
```

### Step 2: Run Tests on Specific Browser
Run tests only on Chromium:
```
pytest --browser=chromium
```

Run tests only on Firefox:
```
pytest --browser=firefox
```

### Step 3: Run Specific Test File
```
pytest tests/test_ui_validation.py
```

### Step 4: Run Specific Test
```
pytest tests/test_ui_validation.py::test_header_text_and_styling
```

### Step 5: Run Tests in Headless Mode
```
pytest --headed=false
```

### Step 6: Run Tests with Custom Parallel Workers
```
pytest -n 4
```

### Step 7: Run Tests in Debug Mode
```
pytest -s -v
```
- `-s`: Show print statements
- `-v`: Verbose output

### Step 8: Run Tests with Specific Markers
```
## 📊 Test Reports

### HTML Report

After running tests, access the HTML report:
```
reports/assignment.html
```

**How to View:**
1. Open the file in a web browser
2. Review test results, execution time, and screenshots

### Allure Report

Generate and view Allure report:

```bash
# Generate Allure report
allure generate reports/allure-results -o reports/allure-report --clean

```

**Installation of Allure CLI:**
Download from: https://github.com/allure-framework/allure2/releases
reports/screenshots/


## ✨ Framework Features

### Page Object Model (POM)
All page interactions are encapsulated in page classes:
- **BasePage:** Common functionality and helper methods
- **TodoPage:** TodoMVC-specific page methods

### Fixtures
pytest fixtures defined in `conftest.py`:
- Browser context setup/teardown
- Automatic screenshots
- HTML and Allure report generation

### Utilities
Reusable utility modules:
- **data_reader.py:** Read test data from JSON files

### Test Coverage

The framework tests:

| Test Category | Coverage |
|---------------|----------|
| **UI Validation** | Header text, styling, input fields, placeholders |
| **Functionality** | Add todos, delete todos, mark complete |
| **Filter Tabs** | All, Active, Completed filters |
| **Clear Completed** | Clear completed todos functionality |
| **Checkbox Interaction** | Mark/unmark todos |
| **Delete Button** | Hover effects, delete functionality |
| **Footer Visibility** | Footer visibility based on state |
| **Tab Navigation** | Navigation between filter tabs |

---

## 🔧 Troubleshooting

### Issue: Playwright browsers not installed
**Solution:**
```bash
playwright install
```

### Issue: Port already in use
**Solution:** The tests use the provided URL, no local server needed.

### Issue: Tests failing due to timeouts
**Solution:** Increase timeout in page object methods or adjust in conftest.py

### Issue: Screenshots not generating
**Solution:** Ensure `reports/screenshots/` directory exists or will be created automatically

---

## 📝 Best Practices

1. **Use Page Objects:** Always create page objects for new pages
2. **Data-Driven Tests:** Use `testdata/data.json` for test data
3. **Explicit Waits:** Use Playwright's built-in waiting mechanisms
4. **Meaningful Assertions:** Use clear assertion messages
5. **Test Independence:** Each test should be independent
6. **Code Reusability:** Put common methods in `BasePage`

---

## 🤝 Contributing

When adding new tests:
1. Create page objects in `pages/` directory
2. Add test data to `testdata/data.json`
3. Write tests in appropriate test file
4. Ensure tests pass locally before committing
5. Update documentation

---

## 📞 Support

For issues or questions:
1. Check pytest documentation: https://docs.pytest.org/
2. Check Playwright documentation: https://playwright.dev/python/
3. Check Allure documentation: https://docs.qameta.io/allure/

---

## 📄 License

This project is part of the automation training assignment.

---

**Last Updated:** December 2025
