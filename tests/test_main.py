"""
Module for functional test cases of main script.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_server_status():
    """Tests if server is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "API server is running"}
