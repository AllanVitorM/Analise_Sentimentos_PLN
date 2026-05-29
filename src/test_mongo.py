from pymongo import MongoClient
from src.config import MONGO_URI, MONGO_DB_NAME

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000
)

print("Tentando conectar...")

client.admin.command("ping")

print("MongoDB conectado com sucesso!")

db = client[MONGO_DB_NAME]
collection = db["analyses"]

result = collection.insert_one({
    "texto": "teste",
    "sentimento": "neutro"
})

print("Documento salvo com ID:", result.inserted_id)