import pytest
from fastapi.testclient import TestClient
from metrichub import app


@pytest.fixture
def client():
    return TestClient(app)
