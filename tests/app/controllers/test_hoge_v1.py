import pytest
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

@pytest.mark.parametrize("i", [4, 5, 6])
def test_hoge_v1(i):
    response = client.post("/hoge_v1", json={"addValue": i})
    print(response.json())
    assert response.status_code == 200
