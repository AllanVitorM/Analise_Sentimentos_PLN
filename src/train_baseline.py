import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

from config import PROCESSED_DATASET_PATH, MODEL_PATH

def treinar_modelo():
    df = pd.read_csv(PROCESSED_DATASET_PATH)
    
    x = df["texto"]
    y = df["sentimento"]
    
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )
    
    modelo = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=30000, ngram_range=(1,2))),
        ("clf", LogisticRegression(max_iter=1000, class_weight="balanced"))
    ])
    
    modelo.fit(x_train, y_train)
    
    predicoes = modelo.predict(x_test)
    
    print("Acurácia: ", accuracy_score(y_test, predicoes))
    print(classification_report(y_test, predicoes))
    
    joblib.dump(modelo, MODEL_PATH)
    
    print(f"Modelo salvo em: {MODEL_PATH}")
    
if __name__ == "__main__":
    treinar_modelo()