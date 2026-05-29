from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)

@patch("src.api.analyses_collection")
@patch("src.api.analisar_emocoes")
def test_predict_retornando_sentimentos(mock_emocoes, mock_collection):
    mock_emocoes.return_value = {
        "aspectos_detectados": [{
            "nome": "frustração",
            "intensidade": 80
        }]
    }
    
    mock_insert = MagicMock()
    mock_insert.inserted_id = "123"
    mock_collection.insert_one.return_value = mock_insert
    
    response = client.post("/predict", json={
        "texto": "produto chegou atrasado e veio com defeito"
    })
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["texto"] == "produto chegou atrasado e veio com defeito"
    assert "sentimento" in data
    assert "confianca" in data
    assert "aspectos_detectados" in data
    assert "_id" in data
    