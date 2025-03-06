
import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Configure pytest to add custom markers.
    
    :param config: Pytest configuration object
    """
    config.addinivalue_line(
        "markers", "smoke: mark test as smoke test"
    )
