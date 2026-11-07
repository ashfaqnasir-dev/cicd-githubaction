import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as test_client:
        yield test_client

def test_home_page(client):
    """Verify that the home page returns an HTTP 200 status code."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"CI/CD Automated Deployment" in response.data

def test_health_check(client):
    """Verify that the health check endpoint returns status ok."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json["status"] == "ok"

