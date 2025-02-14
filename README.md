# sentiment-analysis-on-dana-application-review

In this project We'll be using NLP algorithm to predict the sentiment on [DANA's](https://play.google.com/store/apps/details?id=id.dana) review, regardless of the app version or the review period,  we'll use the most relevant review from google play scaper.
I include clear step-by-step machine learning pipeline on crafting model such as data gathering, data cleaning, data preprocessing, feature extraction, modeling, evaluation, etc.
The label we use here are based on Lexicon analysis in which generate 3 difference label Positive, Negative, and Neutral. I employed Class Weight method for dealing with imabalance data.
The NLP we employ here are LSTM combined with various of Feature Extraction methods, including Word Embedding using Word2Vector and TF-IDF.

Before continue with this file, we should gather all the data we need in from file [slang_word_data_gathering.ipynb](slang_word_data_gathering.ipynb), and then [data_scraping.ipynb](data_scraping.ipynb), and then [sentiment_analysis.ipynb](sentiment_analysis.ipynb)