import os
import sys

import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    layout="centered"
)

DARK = "#2E2910"
GREEN = "#2C5745"
BACKGROUND = "#EBE3A7"
ORANGE = "#EB7D00"

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {BACKGROUND};
    }}

     [data-testid="stForm"] {{
        border: 2px solid black;
        border-radius: 8px;
        padding: 20px;
    }}

    .block-container {{
        max-width: 900px;
        padding-top: 40px;
    }}

    h1, h2, h3, p, label {{
        color: {DARK} !important;
    }}

    .title {{
        text-align: center;
        color: {DARK};
        font-size: 36px;
        font-weight: bold;
    }}

    .subtitle {{
        text-align: center;
        color: {GREEN};
        font-size: 17px;
        margin-bottom: 30px;
    }}

    .result {{
        background-color: {BACKGROUND};
        border: 2px solid {GREEN};
        border-top: 5px solid {ORANGE};
        border-radius: 8px;
        padding: 25px;
        text-align: center;
        margin-top: 25px;
    }}

    .result-title {{
        color: {GREEN};
        font-size: 17px;
        font-weight: 600;
    }}

    .price {{
        color: {ORANGE};
        font-size: 32px;
        font-weight: bold;
        margin-top: 10px;
    }}

    .stFormSubmitButton button {{
        background-color: {ORANGE};
        color: {DARK};
        border: none;
        font-weight: bold;
    }}

    .stFormSubmitButton button:hover {{
        background-color: {GREEN};
        color: {BACKGROUND};
    }}

    </style>
    """,
    unsafe_allow_html=True
)


SOURCE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "source"
    )
)

if SOURCE_DIR not in sys.path:
    sys.path.insert(0, SOURCE_DIR)

try:
    from predict import predict_price
except Exception as e:
    predict_price = None
    import_error = e

st.markdown(
    '<div class="title">House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict the price of a house using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

if predict_price is None:

    st.error(
        "Unable to load the prediction model. "
        "Please check source/predict.py."
    )


with st.form("house_form"):

    st.subheader("House Information")

    col1, col2 = st.columns(2)

    with col1:

        area = st.number_input(
            "Area (m²)",
            min_value=1,
            value=5000,
            step=50
        )

        bedrooms = st.number_input(
            "Bedrooms",
            min_value=1,
            max_value=20,
            value=3
        )

        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1,
            max_value=20,
            value=2
        )

        stories = st.number_input(
            "Stories",
            min_value=1,
            max_value=10,
            value=2
        )

        parking = st.number_input(
            "Parking spaces",
            min_value=0,
            max_value=10,
            value=1
        )

    with col2:

        mainroad = st.selectbox(
            "Main road access",
            ["Yes", "No"]
        )

        guestroom = st.selectbox(
            "Guest room",
            ["Yes", "No"]
        )

        basement = st.selectbox(
            "Basement",
            ["Yes", "No"]
        )

        hotwaterheating = st.selectbox(
            "Hot water heating",
            ["Yes", "No"]
        )

        airconditioning = st.selectbox(
            "Air conditioning",
            ["Yes", "No"]
        )

    st.subheader("Additional Information")

    col3, col4 = st.columns(2)

    with col3:

        prefarea = st.selectbox(
            "Preferred area",
            ["Yes", "No"]
        )

    with col4:

        furnishingstatus = st.selectbox(
            "Furnishing status",
            [
                "Furnished",
                "Semi-furnished",
                "Unfurnished"
            ]
        )

    predict_button = st.form_submit_button(
        "Predict Price",
        use_container_width=True
    )


if predict_button and predict_price is not None:

    mainroad = 1 if mainroad == "Yes" else 0
    guestroom = 1 if guestroom == "Yes" else 0
    basement = 1 if basement == "Yes" else 0
    hotwaterheating = 1 if hotwaterheating == "Yes" else 0
    airconditioning = 1 if airconditioning == "Yes" else 0
    prefarea = 1 if prefarea == "Yes" else 0


    furnished = (
        1 if furnishingstatus == "Furnished" else 0
    )

    semi_furnished = (
        1 if furnishingstatus == "Semi-furnished" else 0
    )

    unfurnished = (
        1 if furnishingstatus == "Unfurnished" else 0
    )

    features = [
        area,
        bedrooms,
        bathrooms,
        stories,
        mainroad,
        guestroom,
        basement,
        hotwaterheating,
        airconditioning,
        parking,
        prefarea,
        furnished,
        semi_furnished,
        unfurnished
    ]


    try:

        prediction = predict_price(features)

        prediction = float(prediction)

        st.success(f"Estimated House Price: {prediction:,.2f}")


    except Exception as e:

        st.error(
            f"Prediction error: {e}"
        )

