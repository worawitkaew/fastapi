
import pytest
from fastapi.testclient import TestClient

from ..main import app
# with TestClient(app) as temp :
#     test_client = temp

@pytest.fixture
def test_client():
    # run this before running tests (setup db)
    with TestClient(app) as temp:
        yield temp
    # run this after running tests (destroy db)