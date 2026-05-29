import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, model_validator

from src.config import MODEL_PATH
from src.openai_emotion_service import analisar_emocoes


app = FastAPI(title="API para Análise de sentimentos de E-commerce")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

modelo = joblib.load(MODEL_PATH)

class ReviewRequest(BaseModel):
    texto: str | None = None
    text: str | None = None

    @model_validator(mode="after")
    def normalizar_texto(self):
        texto = self.texto.strip() if self.texto else None
        text = self.text.strip() if self.text else None

        self.texto = texto or text

        if not self.texto:
            raise ValueError("Informe o campo 'text' ou 'texto'.")

        return self

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
