import joblib

from src.config import MODEL_PATH

def carregar_modelo():
    return joblib.load(MODEL_PATH)

def prever_sentimento(texto):
    modelo = carregar_modelo()
    
    sentimento = modelo.predict([texto])[0]
    probabilidades = modelo.predict_proba([texto])[0]
    
    classes = modelo.classes_
    confiancas = dict(zip(classes, probabilidades))
    
    return sentimento, confiancas

if __name__ == "__main__":
    texto = input("Digite uma avaliação: ")
    sentimento, confiancas = prever_sentimento(texto)
    
    print("\nResultado: ")
    print(f"Sentimento: {sentimento}")
    
    print("\nConfiança por classe: ")
    for classe, prob in confiancas.items():
        print(f"{classe}: {prob:.2%}")
        