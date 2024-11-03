# Anthill UI Testing 🖥️

### Project Overview
This project automates UI testing for the **Anthill** platform, a web application that supports task and project management. Using **Selenium** and **Python**, the tests validate key functionalities like user interactions, form submissions, and navigation flows to ensure a seamless user experience.

### Project Structure
- **locators/**: Contains element locators for each page, grouped by page-specific locator files for easy maintenance.
- **pages/**: Contains files for each page of the web application, with methods representing user actions (e.g., filling forms, clicking buttons, verifying elements).
- **tests/**: Contains test files for each page, validating the logic and interactions defined in the corresponding page files.
- **result/**: Stores Allure reports generated after each test run, providing a detailed view of test results and insights.

### Key Features
Automated tests cover core UI functionality such as:
- Form submissions
- Page navigations
- Error handling and validation
- Modular design: reusable methods for each page
- Test reporting using **pytest** and **Allure**

### Tech Stack
- **Python**
- **Selenium WebDriver**
- **pytest** for running tests and generating reports
- **Allure** for comprehensive test reporting

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/YourUsername/BlaBla-UI-Tests.git
    cd BlaBla-UI-Tests
    ```

2. **Install dependencies**:
    Ensure you have Python and pip installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the tests**:
    Execute all tests using **pytest**:
    ```bash
    pytest
    ```

4. **Generate a test report**:
    To create a detailed Allure report, run:
    ```bash
    pytest --alluredir=result
    allure serve result
    ```

### How It Works
- **locators/**: Each file in the locators folder contains element locators for a specific page, supporting consistency and ease of updates.
- **pages/**: Each file in the pages folder represents a page class with:
  - Methods for interacting with UI elements (e.g., filling forms, clicking buttons)
  - Helper methods to validate page states
- **tests/**: Each file in the tests folder corresponds to a specific page and includes test cases to validate that page’s functionality. Tests leverage methods from the pages folder.

### Example Usage
To run a specific test, specify the test file path:
```bash
pytest tests/test_login_page.py
```
This runs the test suite for the login page, ensuring that functionalities like successful login and error messaging work as expected.

### Continuous Integration

This project can be integrated with **GitHub Actions** for automated testing on each new commit.

### Contributing

To contribute to this project:
- Fork the repository.
- Create a feature branch: (`git checkout -b feature-name`).
- Commit your changes (`git commit -m 'Add feature'`).
- Push to the branch (`git push origin feature-name`).
- Open a pull request for review.

---

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Future Enhancements
- Adding complex, multi-step test cases
- Integrating with a CI/CD pipeline for automated testing on new commits


This README now includes the **result** folder section, clarifying Allure report generation. Feel free to let me know if you need more adjustments!


---
