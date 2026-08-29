import joblib
model = joblib.load("models/house_price_model.pkl")


def predict_price(features):
    """
    Prédit le prix d'une maison.
    """
    prediction = model.predict([features])

    return prediction[0]

