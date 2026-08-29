House Price Prediction
Project Overview

House Price Prediction is a Machine Learning project that predicts the price of a house based on its characteristics.

The project uses Linear Regression to learn the relationship between house features and their prices. A Streamlit web application is also provided to allow users to enter house information and obtain a price prediction.

Objectives

The main objectives of this project are:

Analyze a house price dataset.
Perform data cleaning and preprocessing.
Explore the relationships between house features and prices.
Encode categorical variables into numerical values.
Train a Machine Learning regression model.
Evaluate the model using regression metrics.
Save the trained model for later use.
Build a simple web application with Streamlit for house price prediction.
Dataset

The project uses the Housing.csv dataset.

The dataset contains 545 houses and the following features:

area — House area
bedrooms — Number of bedrooms
bathrooms — Number of bathrooms
stories — Number of stories
mainroad — Main road access
guestroom — Guest room availability
basement — Basement availability
hotwaterheating — Hot water heating availability
airconditioning — Air conditioning availability
parking — Number of parking spaces
prefarea — Preferred area
furnishingstatus — Furnishing status
price — House price

The original dataset contains prices expressed in Pakistani Rupees (PKR).

Data Preprocessing

The following preprocessing steps were performed:

Loaded the dataset using Pandas.
Checked the structure and information of the dataset.
Analyzed the distribution of house prices.
Explored relationships between features and price.
Converted binary categorical variables:
yes → 1
no → 0
Applied One-Hot Encoding to furnishingstatus.
Separated the features (X) from the target (y).
Split the dataset into training and testing sets.

The dataset was divided into:

80% training data → 436 houses
20% testing data → 109 houses
Exploratory Data Analysis

Several visualizations were used to understand the dataset, including:

House price distribution
Area versus price
Price distribution by number of bedrooms

The analysis showed that house prices are right-skewed, with most prices concentrated in the lower and middle range and a smaller number of expensive houses.

Machine Learning Model

The selected model is:

Linear Regression

Linear Regression was chosen as the main model because the objective is to predict a continuous numerical value: the house price.

The model was trained using the training dataset and then evaluated using the testing dataset.

Model Evaluation

The model was evaluated using:

Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
R² Score
Results
Metric	Result
MAE	970,043.40
RMSE	1,324,506.96
R² Score	0.653

The R² score of approximately 0.653 means that the model explains around 65.3% of the variation in house prices on the test dataset.

Model Saving

After training, the Linear Regression model is saved using joblib.

The saved model is stored in:

models/house_price_model.pkl

The .pkl file contains the trained Machine Learning model, allowing it to be loaded later without training the model again.

Prediction

The prediction process works as follows:

Load the trained model.
Receive the characteristics of a house.
Convert categorical values into numerical values.
Arrange the features in the same order used during training.
Pass the features to the trained model.
Generate the predicted house price.

The prediction function is located in:

source/predict.py
Streamlit Application

A simple web interface was developed using Streamlit.

The application allows users to enter:

Area
Number of bedrooms
Number of bathrooms
Number of stories
Main road access
Guest room
Basement
Hot water heating
Air conditioning
Parking spaces
Preferred area
Furnishing status

After clicking Predict Price, the application returns the estimated house price.

Technologies Used

Programming Language
Python

Data Science
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn

Machine Learning
Linear Regression

Application
Streamlit

Model Persistence
Joblib

Development Tools
VS Code

Example Prediction

Example input:

Area: 5000 m²
Bedrooms: 3
Bathrooms: 2
Stories: 2
Parking spaces: 1
Main road access: Yes
Guest room: No
Basement: No
Hot water heating: No
Air conditioning: Yes
Preferred area: Yes
Furnishing status: Furnished

The application then returns an estimated house price based on the trained Linear Regression model.

Author

Mhammed Benabderrahman

Data Science graduate interested in Data Science, Machine Learning and Data Analysis.

License

This project is licensed under the MIT License.