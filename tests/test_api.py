from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)

def test_home_retorno_api():
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json()["message"] == "API Funcionando"
    
    
def test_predict_retorno_erro_vazio():
    response = client.post("/predict", json={"texto" : ""})
    
    assert response.status_code in [400, 422]
    
    

    