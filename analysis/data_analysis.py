import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/original/Housing.csv")

print(df.head())

print(df.describe())

missing = df.isnull().sum()
print(missing[missing > 0])

print("Nombre de doublons :", df.duplicated().sum())

# Elle cherche les colonnes contenant des données de type texte/catégorie
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts())

# le graphique de distribution des prix
plt.figure(figsize=(8, 5))
sns.histplot(df["price"], kde=True) #  kde=True ajoute une courbe représentant approximativement la distribution.
plt.title("Distribution des prix des maisons")
plt.xlabel("Prix")
plt.ylabel("Nombre de maisons")
plt.tight_layout() # Ajuste automatiquement les éléments du graphique pour éviter qu'ils se chevauchent.
plt.savefig("results/figures/price_distribution.png")
plt.show()

# Distribution de la superficie
plt.figure(figsize=(8, 5))
sns.histplot(df["area"], kde=True)
plt.title("Distribution de la superficie")
plt.xlabel("Superficie")
plt.ylabel("Nombre de maisons")
plt.tight_layout()
plt.savefig("results/figures/area_distribution.png")
plt.show()

# Relation entre superficie et prix
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="area", y="price")
plt.title("Relation entre superficie et prix")
plt.xlabel("Superficie")
plt.ylabel("Prix")
plt.tight_layout()
plt.savefig("results/figures/area_vs_price.png")
plt.show()

# Prix selon le nombre de chambres
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="bedrooms", y="price")
plt.title("Prix selon le nombre de chambres")
plt.xlabel("Nombre de chambres")
plt.ylabel("Prix")
plt.tight_layout()
plt.savefig("results/figures/bedrooms_vs_price.png")
plt.show()

# Sélectionner les colonnes numériques
df_numeric = df.select_dtypes(include="number")

# la matrice de corrélation
plt.figure(figsize=(10, 7))
sns.heatmap(
    df_numeric.corr(),
    annot=True, # Affiche les valeurs directement dans les cases.
    fmt=".2f",
    cmap="coolwarm" # Définit la palette de couleurs de la heatmap.
)

plt.title("Matrice de corrélation")
plt.tight_layout()
plt.savefig("results/figures/correlation_matrix.png")
plt.show()
