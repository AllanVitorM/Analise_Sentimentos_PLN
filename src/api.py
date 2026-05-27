import joblib
from fastapi import FastAPI
from pydantic import BaseModel

from src.config import MODEL_PATH
from src.openai_emotion_service import analisar_emocoes


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
    probabilidades = modelo.predict_proba([review.texto])[0]
    
    classes = modelo.classes_
    confiancas = dict(zip(classes, probabilidades))
    
    aspectos = analisar_emocoes(review.texto)

    try:
        aspectos = analisar_emocoes(review.texto)
        aspectos_detectados = aspectos.get("aspectos_detectados", [])
    except Exception:
        aspectos_detectados = []

    return {
        "texto": review.texto,
        "sentimento": sentimento,
        "confianca": round(float(max(confiancas.values())), 4),

        "aspectos_detectados": aspectos_detectados
    }