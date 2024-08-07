import pandas as pd
from KMeans import KMeans

# 1. Încărcarea setului de date
iris_data = pd.read_csv('iris.data', header=None)

# 2. Eliminați ultima coloană
iris_features = iris_data.iloc[:, :-1]

# 3. Normalizarea caracteristicilor
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
iris_features_normalized = scaler.fit_transform(iris_features)

# 4. Implementarea algoritmului k-means

# from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(iris_features_normalized)

# 5. Prezicerea clusterelor pentru noi exemple
new_example = [[5.1, 3.5, 1.4, 0.2]]  # Exemplu de caracteristici
new_example_normalized = scaler.transform(new_example)
predicted_cluster = kmeans.predict(new_example_normalized)
print("Predicted cluster:", predicted_cluster)

# 6. Evaluarea performanței pe datele de antrenare
train_labels = kmeans.labels_
print("Train labels:", train_labels)
