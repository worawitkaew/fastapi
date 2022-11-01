
import pytest

from ..main import app
from fastapi.testclient import TestClient

@pytest.fixture
def test_client():
    # run this before running tests (setup db)
    with TestClient(app) as temp:
        yield temp
    # run this after running tests (destroy db)



    
@pytest.mark.asyncio
async def test_ProductType1(test_client):

    response = await test_client.get("/")
    assert response.json() == {
    "message": "Hello Worl"
    }
