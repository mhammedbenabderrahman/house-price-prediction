import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import joblib


df = pd.read_csv("data/cleaned/Housing_cleaned.csv")

# Variables explicatives X
X = df.drop("price", axis=1)

# Variable cible y
y = df["price"]

print("Dimensions de X :", X.shape)
print("Dimensions de y :", y.shape)

print("\nColonnes de X :", X.columns.tolist())

print("\nVariable cible :", y.name)

print ("\nSéparer les données en entraînement et test")
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train :", X_train.shape)
print("X_test  :", X_test.shape)
print("y_train :", y_train.shape)
print("y_test  :", y_test.shape)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Premières prédictions :", y_pred[:5])

print("\nVrais prix :", y_test.head().values)

# Évaluer le modèle
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n--- Évaluation du modèle ---")
print("MAE  :", mae)
print("MSE  :", mse)
print("RMSE :", rmse)
print("R²   :", r2)

# Sauvegarder le modèle
joblib.dump(model, "models/house_price_model.pkl")
