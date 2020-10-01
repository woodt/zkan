import pytest
from fastapi.testclient import TestClient

from zkan import app


@pytest.mark.db
def test_schema_list():
    with TestClient(app) as client:
        response = client.get("/schemas")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
