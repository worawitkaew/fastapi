
import pytest

from ..main import app
# from .test_main import test_client

from fastapi.testclient import TestClient

@pytest.fixture
def test_client():
  
    client = TestClient(app)
    return client
  



    
@pytest.mark.asyncio
def test_ProductType1(test_client):

    response = test_client.get("/")
    assert response.json() == {
    "message": "Hello World"
    }
