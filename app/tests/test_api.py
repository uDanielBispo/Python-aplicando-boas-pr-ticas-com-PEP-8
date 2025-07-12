import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'msg': 'Bem-vindo à API de Recomendação de Produtos'}

def test_criar_produtos():
    response = client.post()



