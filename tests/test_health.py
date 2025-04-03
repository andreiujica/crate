from fastapi import status


def test_health_endpoint(client):
    """
    Test the health endpoint returns 200 OK and the expected response.
    """
    response = client.get("/health")
    
    # Check status code
    assert response.status_code == status.HTTP_200_OK
    
    # Check response content
    assert response.text == '"OK"'