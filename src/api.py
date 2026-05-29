import joblib
from fastapi import FastAPI
from fastapi import HTTPException
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, model_validator
from src.database import analyses_collection
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

    
    try:
        sentimento = modelo.predict([review.texto])[0]
        probabilidades = modelo.predict_proba([review.texto])[0]
        
        classes = modelo.classes_
        confiancas = dict(zip(classes, probabilidades))
    except Exception:
        raise HTTPException(status_code=500,
                            detail="Erro ao executar o modelo de sentimentos"
            )

    try:
        aspectos = analisar_emocoes(review.texto)
        aspectos_detectados = aspectos.get("aspectos_detectados", [])
    except Exception:
        aspectos_detectados = []
        
    resultado = {
        "texto": review.texto,
        "sentimento": sentimento,
        "confianca": round(float(max(confiancas.values())), 4),

        "aspectos_detectados": aspectos_detectados,
        "created_at": datetime.now(timezone.utc)
    }
    
    try:
        insert_result = analyses_collection.insert_one(resultado)
        
    except Exception as error:
        print("ERRO AO SALVAR NO MONGO:", error)
        raise HTTPException(
            status_code=500,
            detail="Erro ao salvar análise no banco de dados"
        )

    resultado["_id"] = str(insert_result.inserted_id)
    resultado["created_at"] = resultado["created_at"].isoformat()
    
    return resultado

@app.get("/analyses")
def list_analyses():
    analyses = []

    for item in analyses_collection.find().sort("created_at", -1).limit(20):
        item["_id"] = str(item["_id"])

        if "created_at" in item and hasattr(item["created_at"], "isoformat"):
            item["created_at"] = item["created_at"].isoformat()

        analyses.append(item)

    return {
        "total": len(analyses),
        "data": analyses
    }