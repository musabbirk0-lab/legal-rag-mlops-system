from fastapi.testclient import TestClient
from app.app import app


client = TestClient(app)


def test_upload_endpoint():
response = client.get('/query?q=test')
assert response.status_code == 200
