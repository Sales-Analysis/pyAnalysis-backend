from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


class TestGroup:
    def test_endpoint_get(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello"}

    def test_get_analysis_positive(self):
        response = client.get("/analysis/ABC")
        assert response.status_code == 200
        assert response.json() == {"message": "hello world"}

    def test_get_analysis_negative(self):
        response2 = client.get("/analysis/A")
        assert response2.status_code == 400
        assert response2.json() == {'error': 'analysis not found'}

    def test_get_report(self):
        response = client.get("/report")
        assert response.status_code == 200
        assert int(dict(response.headers).get('content-length')) > 1000
        # response.read().decode('utf-8')
