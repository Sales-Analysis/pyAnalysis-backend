from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


class TestGroup():
    def test_endpoint_get(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello"}

    def test_endpoint_get_analysis(self):
        response = client.get("/analysis/ABC")
        assert response.status_code == 200
        assert response.json() == {"message": "hello world"}
        response2 = client.get("/analysis/A")
        assert response2.status_code == 400
        assert response2.json() == {'error': 'analysis not found'}
