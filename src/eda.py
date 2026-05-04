import pandas as pd

dataset = "data/olist_order_reviews_dataset.csv"

df = pd.read_csv(dataset)

print("primeiras linhas: ")
print(df.head())

print("\nInformações do dataset: ")
print(df.info())

print("\nDistribuição das notas: ")
print(df["review_score"].value_counts().sort_index())

print("\nQuantidade de comentários vazios: ")
print(df["review_comment_message"].isna().sum())

print("\nTotal de registros: ")
print(len(df))