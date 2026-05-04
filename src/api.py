import joblib
from fastapi import FastAPI
from pydantic import BaseModel

from config import MODEL_PATH

app = FastAPI(title="API para Análise de sentimentos de E-commerce")

modelo = joblib.load(MODEL_PATH)

class ReviewRequest(BaseModel):
    texto: str

@app.get("/")
def home():
    return{
        "message": "API Funcionando"
    }
    
@app.post("/predict")
def predict(review: ReviewRequest):
    sentimento = modelo.predict([review.texto])[0]
    probabilidades = modelo.predict_prob([review.texto])[0]
    
    classes = modelo.classes_
    confiancas = dict(zip(classes, probabilidades))
    
    return {
        "texto": review.texto,
        "sentimento": sentimento,
        "confianca": round(max(probabilidades), 4),
        "probabilidades": {
            classe: round(float(prob), 4)
            for classe, prob in confiancas.items()
        }
    }