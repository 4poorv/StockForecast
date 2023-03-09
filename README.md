# Stock Price Prediction using Machine Learning
This project aims to predict stock prices using machine learning algorithms. The project leverages historical data on stock prices, as well as technical indicators like the Relative Strength Index (RSI) and Moving Average Convergence Divergence (MACD) to identify patterns and trends in the data. Additionally, it collects tweets related to specific stock tickers and uses Natural Language Processing (NLP) techniques to analyze the sentiment.

## Data Collection
Historical stock price data is collected from various sources such as Yahoo Finance, Google Finance, Alpha Vantage, and Quandl. Tweets are collected using Twitter API, and the collected data is cleaned and preprocessed to remove errors and handle missing values.

## Feature Engineering
The relevant features such as opening price, closing price, highest price, lowest price, volume, moving averages, Relative Strength Index (RSI), and Moving Average Convergence Divergence (MACD) are extracted from the data.

## Data Preprocessing
The data is preprocessed to make it suitable for machine learning models. Preprocessing involves cleaning the data, handling missing values, scaling the data, and splitting it into training and testing sets. The data is scaled to ensure that all the features are in the same range.

## Model Selection
Several machine learning models can be used for predicting stock prices, including Linear Regression, Random Forests, Support Vector Machines (SVMs), and Recurrent Neural Networks (RNNs). The choice of model depends on the type of data and the level of accuracy required.

## Model Training
The selected machine learning model is trained on the training data. During the training process, the model learns the patterns in the data and adjusts its parameters to minimize the error between the predicted and actual values. Cross-validation techniques are used to validate the model's performance to ensure that the model is not overfitting or underfitting the data.

## Model Evaluation
The trained model's performance is evaluated on the test data using various evaluation metrics like Mean

## Model Deployment
The trained model is deployed to make predictions on new data. The collected tweets are analyzed using NLP techniques to determine the sentiment and its effect on stock prices.

# References
1. Alpha Vantage. (n.d.). Alpha Vantage API Documentation `<link>` : https://www.alphavantage.co/documentation/
2. Brownlee, J. (2021). How to Develop a Deep Learning Model for Stock Price Prediction. Machine Learning Mastery. `<link>` : https://machinelearningmastery.com/how-to-develop-deep-learning-models-for-univariate-time-series-forecasting/
3. Google Finance. (n.d.). `<link>` : https://www.google.com/finance
4. Quandl. (n.d.). Quandl API Documentation. `<link>` : https://docs.quandl.com/
5. Twitter Developer Platform. (n.d.). Twitter API Documentation. `<link>` : https://developer.twitter.com/en/docs/twitter-api

