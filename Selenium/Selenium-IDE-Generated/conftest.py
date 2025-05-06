# conftest.py
import pytest


def pytest_addoption(parser):
    """
    This function is a hook for adding custom command-line options to pytest.
    """
    parser.addoption(
        "--range-limit",  # The command-line argument to add
        action="store",  # Action to take: 'store' means it stores the argument value
        default=10,  # Default value if the argument is not provided
        type=int,  # Expected type of the argument value
        help="The upper limit for the parameter range.",  # Help message for the argument
    )


@pytest.fixture
def range_limit(request):
    """
    A pytest fixture that fetches the value of the custom command-line option '--range-limit'.
    """
    return request.config.getoption("--range-limit")
