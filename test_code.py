# Test file for pytest. This example includes several test functions and uses pytest fixtures for setup and teardown.

import pytest

# "Fixture for setup and cleanup".
@pytest.fixture
def setup_data():
    print("\nSetup")
    data = {"key1": "value1", "key2": "value2"}
    yield data
    print("\nCleanup")

#  "Test function using the fixture."
def test_key1(setup_data):
    assert setup_data["key1"] == "value1"

# "Another test function using the fixture"
def test_key2(setup_data):
    assert setup_data["key2"] == "value2"

# "Test function without using the fixture"
def test_addition():
    assert 1 + 1 == 2
