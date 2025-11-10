from flask import Flask
import pytest
from ACEest_Fitness import app  # Use correct import

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Fitness" in rv.data
