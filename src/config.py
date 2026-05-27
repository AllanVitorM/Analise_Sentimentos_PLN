from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
MODELS_DIR = BASE_DIR / "models"

DATASET_PATH = DATA_DIR / "olist_order_reviews_dataset.csv"
PROCESSED_DATASET_PATH = DATA_DIR / "reviews_tratados.csv"

MODEL_PATH = MODELS_DIR / "sentiment_model.pkl"

OPEN_API_KEY = os.getenv("OPENAI_API_KEY")