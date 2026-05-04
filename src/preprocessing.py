import pandas as pd
from config import DATASET_PATH, PROCESSED_DATASET_PATH

def mapear_sentimento(score): 
    try:
        score = int(score)
    except ValueError:
        return "invalido"

    if score < 1 or score > 5:
        return "invalido"
    
    if score <= 2:
        return "negativo"
    elif score == 3:
        return "neutro"
    else: 
        return "positivo"
    
def preparar_dados():
    df = pd.read_csv(DATASET_PATH)
    df["texto"] = (
        df["review_comment_title"].fillna("")+ " " +
        df["review_comment_message"].fillna("")
    ).str.strip()
    
    df = df[df["texto"] != ""]
    
    df["sentimento"] = df["review_score"].apply(mapear_sentimento)
    df = df[df["sentimento"] != "invalido"]
    
    df_final = df[["texto", "review_score", "sentimento"]]
    
    df_final.to_csv(PROCESSED_DATASET_PATH, index=False)
    
    print("Dataset tratado salvo com sucesso")
    print(f"Arquivo salvo em: {PROCESSED_DATASET_PATH}")
    print(f"Total de registros tratados: {len(df_final)}")
    
if __name__ == "__main__":
    preparar_dados()