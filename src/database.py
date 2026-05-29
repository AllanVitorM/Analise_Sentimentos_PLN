from pymongo import MongoClient

from src.config import MONGO_URI, MONGO_DB_NAME

if not MONGO_URI:
    raise RuntimeError("MONGO_URI não configurada")

client = MongoClient(MONGO_URI)

db = client[MONGO_DB_NAME]

analyses_collection = db["analyses"]