import pytest
from fastapi.testclient import TestClient

from src.main import application


@pytest.fixture
def client():
    """
    Create a test client for the FastAPI application.
    """
    return TestClient(application) 