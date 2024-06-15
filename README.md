📊 COVID-19 Sentiment Analysis 🦠
Welcome to the COVID-19 Sentiment Analysis project! This repository contains the code and resources necessary to perform sentiment analysis on COVID-19 related tweets. Our goal is to understand public sentiment during the pandemic using Natural Language Processing (NLP) techniques. 🌍❤️

Project Overview 📁
Main Files 📂
covid19_evolution_and_sentiment_analysis:

This is the main file where we import COVID-19 data (confirmed, recovered, and death cases by country from the covid-19-all dataset) and tweets referring to COVID-19 along with their locations (tweets_train dataset).
Investigations include:
Handling missing values for each dataset.
Analyzing the COVID-19 situation over time and by country.
Examining the sentiment associated with the tweets and its distribution by country to identify any correlation with the most affected countries.
generic_models:

In this file, we define and fit several models to the data after cleaning the tweets (using functions from cleaning_tweets). Models include:
Passive Aggressive Classifier
Logistic Regression
Random Forest
Support Vector Classifier (SVC)
XGBoost
Models are fitted not only to COVID-19 tweets but also to Italian tweets and ChatGPT tweets.
Before fitting each model to the data, the tweets are vectorized using TF-IDF.
cleaning_tweets:

Contains functions to clean the tweets, such as removing punctuation, symbols, and other irrelevant characters to ensure quality and consistency.
find_country:

Contains a function to determine the country from a given location, which is useful for geolocating tweets.
rnn:

Fits a Recurrent Neural Network (RNN) model to the COVID-19 data (not applied to the entire dataset due to memory limitations).
TF-IDF vectorization is used here as well.
Datasets 📊
COVID-19 Dataset:

Contains tweets related to COVID-19. The sentiments in these tweets are categorized into 'Neutral', 'Positive', 'Extremely Negative', 'Negative', 'Extremely Positive'. For analysis, these sentiments are grouped into three categories: 0 (Extremely Negative, Negative), 1 (Neutral), and 2 (Extremely Positive, Positive).
Italian Dataset:

Contains Italian tweets with sentiments categorized into 'NEUTRAL', 'POSITIVE', 'MIXED', 'NEGATIVE'. For analysis, these sentiments are grouped into three categories: 0 (NEGATIVE), 1 (NEUTRAL, MIXED), and 2 (POSITIVE).
ChatGPT Dataset:

Contains tweets mentioning ChatGPT. The sentiments in these tweets are categorized into 'neutral', 'good', 'bad'. For analysis, these sentiments are grouped into three categories: 0 (bad), 1 (neutral), and 2 (good).
Analysis and Models 📈
The project involves several key steps and methodologies:

Data Preprocessing:

Cleaning and preparing the tweet text using the cleaning_tweets module.
Tokenization and vectorization using TF-IDF.
Sentiment Analysis:

Applying various machine learning models to classify the sentiment of tweets. Models include:
Passive Aggressive Classifier
Logistic Regression
Random Forest
Support Vector Classifier (SVC)
XGBoost
Recurrent Neural Network (RNN)
Visualization:

Creating charts and maps to visualize the progression of the pandemic and the distribution of sentiment in tweets.
Analyzing the frequency of tweets over time and the geographical distribution of tweet locations.
Model Evaluation:

Evaluating the performance of the models using metrics such as accuracy, precision, and recall.
Contributions 🤝
Contributions are welcome! If you would like to contribute, please fork the repository and submit pull requests with improvements or bug fixes.

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
Happy coding! 😷📊✨
