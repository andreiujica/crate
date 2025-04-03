from fastapi import status
from fastapi.testclient import TestClient


def test_health_endpoint(client: TestClient) -> None:
    """
    Test the health endpoint returns 200 OK and the expected response.
    """
    response = client.get("/health")
    
    # Check status code
    assert response.status_code == status.HTTP_200_OK
    
    # Check response content
    assert response.text == '"OK"'