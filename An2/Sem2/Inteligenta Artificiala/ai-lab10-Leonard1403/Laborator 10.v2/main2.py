# Invatare nesupervizata cu reprezentare Word Embeddings

import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Read the data
data = pd.read_pickle("merged_training.pkl")

# Train Word2Vec model on the text data
sentences = [text.split() for text in data['text']]
word2vec_model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)

# Extract word embeddings as features for each text
word_embeddings = []
for text in sentences:
    embeddings = [word2vec_model.wv[word] for word in text if word in word2vec_model.wv]
    if embeddings:
        text_embedding = np.mean(embeddings, axis=0)  # Average the word embeddings
    else:
        text_embedding = np.zeros(100)  # If no embeddings found, use zero vector
    word_embeddings.append(text_embedding)

# Scale the word embeddings
scaler = StandardScaler()
scaled_word_embeddings = scaler.fit_transform(word_embeddings)

# Apply K-means clustering on the scaled embeddings
k = 5  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(scaled_word_embeddings)

# Get the predicted clusters for each text
predicted_clusters = kmeans.labels_

# Add the predicted clusters to the dataframe
data['predicted_cluster'] = predicted_clusters

# Print the results
print(data[['text', 'predicted_cluster']])


# Example sentence for prediction
test_sentence = "I won all the games today."
print(test_sentence)

# Preprocess the test sentence
test_sentence = test_sentence.split()

# Generate word embeddings for the test sentence
test_embeddings = [word2vec_model.wv[word] for word in test_sentence if word in word2vec_model.wv]
if test_embeddings:
    test_embedding = np.mean(test_embeddings, axis=0)  # Average the word embeddings
else:
    test_embedding = np.zeros(100)  # If no embeddings found, use zero vector

# Scale the test embedding
scaled_test_embedding = scaler.transform([test_embedding])

# Predict the cluster for the test sentence
predicted_cluster = kmeans.predict(scaled_test_embedding)

# Map the cluster to an emotional label
emotion_labels = {0: "sadness", 1: "love", 2:"anger", 3: "joy", 4: "fear"}
predicted_emotion = emotion_labels[predicted_cluster[0]]

print(f"Predicted Emotion: {predicted_emotion}")