import openpyxl
from io import BytesIO
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

    def test_get_report(self, data_output):
        response = client.get("/report")
        wb = openpyxl.load_workbook(BytesIO(response.read()))
        worksheet = wb.worksheets[0]
        result = [i for i in worksheet.values]
        assert response.status_code == 200
        assert int(dict(response.headers).get('content-length')) > 1000
        assert result == data_output

    def test_upload(self):
        path = "../data/abc_test.xlsx"
        files = {"file": open(path, "rb")}
        requests = client.post("/uploadfile", files=files)
        assert requests.status_code == 200
