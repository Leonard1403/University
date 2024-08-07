# TF-IDF + K-means + Logistic Regression

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from KMeans import KMeans
# from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# Read the data
data = pd.read_csv('reviews_mixed.csv')

# Extract features using TF-IDF representation
tfidf_vectorizer = TfidfVectorizer()
features = tfidf_vectorizer.fit_transform(data['Text'])

# Perform clustering using K-means
k = 2  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
clusters = kmeans.fit_predict(features.toarray())

# Combine the cluster labels and original labels
data['Cluster'] = clusters

# Separate the features and labels for supervised learning
X = features.toarray()
y = data['Sentiment']

# Train a logistic regression classifier on the combined features and labels
classifier = LogisticRegression()
classifier.fit(X, y)

# Make predictions on the training data
predictions = classifier.predict(X)

# Calculate accuracy score
accuracy = accuracy_score(y, predictions)
print("Accuracy:", accuracy)

# Example sentence for prediction
test_sentence = "The staff was bad."
print(test_sentence)

# Extract features for the test sentence
test_features = tfidf_vectorizer.transform([test_sentence])

# Predict the cluster for the test sentence using K-means
test_cluster = kmeans.predict(test_features)[0]

# Predict the sentiment using the trained classifier
test_sentiment = classifier.predict(test_features)[0]

print("Predicted Cluster:", test_cluster)
print("Predicted Sentiment:", test_sentiment)
