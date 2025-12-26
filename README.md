# Playwright_Assignment

A comprehensive Playwright automation framework for testing the TodoMVC application. This project demonstrates a robust, maintainable test framework with cross-browser testing capabilities, detailed reporting, and parallel execution.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Test Reports](#test-reports)
- [Framework Features](#framework-features)

---

## 🎯 Project Overview

This framework is designed to:
- **Test TodoMVC Application** with comprehensive test coverage
- **Support Multiple Browsers** (Chrome, Firefox)
- **Run Tests in Parallel** for faster execution
- **Generate Detailed Reports** using Allure and HTML reports
- **Follow Page Object Model (POM)** design pattern for maintainability
- **Capture Screenshots** for all tests automatically

**Test Application URL:** https://demo.playwright.dev/todomvc/#/

---

## 📦 Prerequisites

Before setting up the project, ensure you have:

- **Python:** 3.8 or higher
- **pip:** Python package manager (comes with Python)
- **Git:** For version control
- **Supports operating systems:** Windows/Linux/Mac

To verify your Python installation, run:
```bash
python --version
pip --version
```

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Playwright_Assignment
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Install Playwright Browsers
After installing the requirements, install the required browsers:
```bash
playwright install
```


## ⚙️ Configuration

### pytest.ini Configuration


**Key Configuration Options:**

| Option | Description |
|--------|-------------|
| `--browser=chromium` | Run tests on Chromium browser |
| `--browser=firefox` | Run tests on Firefox browser |
| `--headed` | Run tests in headed mode (visible browser) |
| `--base-url` | Base URL for the TodoMVC application |
| `--screenshot=on` | Enable automatic screenshots |
| `--tracing=on` | Enable trace recording for debugging |
| `--html=reports/` | Generate HTML report |
| `--alluredir=` | Directory for Allure results |
| `-n 2` | Run 2 parallel workers | 


## 🧪 Running Tests

### Step 1: Basic Test Run
Run all tests with default configuration:
```bash
pytest
```

### Step 2: Run Tests on Specific Browser
```bash
Run
pytest
```

### Step 2: Run Tests on Specific Browser
Run tests only on Chromium:
```bash
pytest --browser=chromium
```

Run tests only on Firefox:
```bash
pytest --browser=firefox
```

### Step 3: Run Specific Test File
```bash
pytest tests/test_ui_validation.py
```

### Step 4: Run Specific Test
```bash
pytest tests/test_ui_validation.py::test_header_text_and_styling
```

### Step 5: Run Tests in Headless Mode
```bash
pytest --headed=false
```

### Step 6: Run Tests with Custom Parallel Workers
```bash
pytest -n 4
```

### Step 7: Run Tests in Debug Mode
- `-s`: Show print statements
- `-v`: Verbose output

```bash
pytest -s -v
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
| **Reset Tab** | Reset all completed todos functionality |
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

### Issue: Tests failing due to timeouts
**Solution:** Increase timeout in page object methods or adjust in conftest.py

---

## 📝 Best Practices

1. **Use Page Object Model:** Always create new class for new page implementation
2. **Data-Driven Tests:** Use `testdata/data.json` for test data
3. **Explicit Waits:** Use Playwright's built-in waiting mechanisms
4. **Meaningful Assertions:** Use clear assertion messages
5. **Test Independence:** Each test should be independent
6. **Code Reusability:** Put common methods in `BasePage`

