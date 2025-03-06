
# Selenium Project for MyHeritage Website

This project contains Selenium tests for automating interactions with the [MyHeritage](https://www.myheritage.co.il/) website. It uses the Page Object Model (POM) design pattern and integrates `pytest-benchmark` for performance testing.

## Project Structure

```
selenium_project/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_home_page.py
│
├── utils/
│   ├── __init__.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.x
- `pip` package manager
- Chrome browser
- ChromeDriver (ensure it's in your PATH or provide the executable path)

### Installation

1. Clone the repository or download the zip file and extract it.
2. Navigate to the project directory.

```bash
cd selenium_project
```

3. Install the required packages.

```bash
pip install -r requirements.txt
```

## Running the Tests

To run the tests using `pytest`, navigate to the project directory and execute the following command:

```bash
pytest
```

This will run all the tests in the `tests` directory and display the results, including the benchmark performance results.

### Running Specific Tests

To run a specific test file:

```bash
pytest tests/test_home_page.py
```

## Project Details

### Page Object Model

- **BasePage**: Contains common methods for interacting with web elements.
- **HomePage**: Represents the home page of the MyHeritage website and contains methods to interact with elements on the home page.

### Tests

- **test_home_page.py**: Contains tests for verifying the search functionality and sign-in functionality on the home page.

### Benchmarking

The project uses `pytest-benchmark` to measure the performance of specific interactions. The benchmark results will be displayed in the test output.

## File Descriptions

- **base_page.py**: Defines the `BasePage` class with common methods for web element interactions.
- **home_page.py**: Defines the `HomePage` class with methods to interact with the home page elements.
- **test_home_page.py**: Contains the test cases for the home page.
- **conftest.py**: Configures pytest and adds custom markers.
- **requirements.txt**: Lists the required Python packages.

## Contact

For any questions or issues, please contact [Your Name](mailto:your.email@example.com).
