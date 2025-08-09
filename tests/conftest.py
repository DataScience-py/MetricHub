"""Create a fixture for the app."""

import pytest
from fastapi.testclient import TestClient

from metrichub import app


@pytest.fixture
def client() -> TestClient:
    """
    Client craete a test client for the app.

    Returns
    -------
    TestClient
        Test client for the app.
    """
    return TestClient(app)
