import pandas as pd

df = pd.read_csv("data/original/Housing.csv")

print("Avant nettoyage :", df.shape)

print("\nValeurs manquantes :", df.isnull().sum())

print("\nDoublons :", df.duplicated().sum())

print("\nTypes des colonnes :", df.dtypes)

print("\nValeurs uniques des colonnes catégorielles :")
for column in df.select_dtypes(include="object").columns:
    print(f"\n{column}:")
    print(df[column].unique())

# Encoder les variables yes/no
binary_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for column in binary_columns:
    df[column] = df[column].map({"yes": 1, "no": 0})


# Encoder furnishingstatus
df = pd.get_dummies(
    df,
    columns=["furnishingstatus"],
    dtype=int
)

print("\nDonnées après encodage :", df.head())
print("\nColonnes :", df.columns.tolist())

# Sauvegarder les données nettoyées
df.to_csv("data/cleaned/Housing_cleaned.csv", index=False)

