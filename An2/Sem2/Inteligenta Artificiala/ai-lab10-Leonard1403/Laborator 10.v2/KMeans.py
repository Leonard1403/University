import numpy as np

class KMeans:
    def __init__(self, n_clusters, random_state=None):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.centroids = None
        self.labels_ = None

    def fit(self, X):
        np.random.seed(self.random_state)
        # Initializare aleatoare a centroizilor
        random_indices = np.random.choice(X.shape[0], self.n_clusters, replace=False)
        self.centroids = X[random_indices]

        while True:
            # Assign clusters
            clusters = self._assign_clusters(X)

            # Update centroids
            new_centroids = self._update_centroids(X, clusters)

            # Verifica daca s-a atins convergenta
            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

        self.labels_ = clusters

    def predict(self, X):
        dense_X = X.toarray()
        distances = np.sqrt(((dense_X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        return np.argmin(distances, axis=1)

    def fit_predict(self, X):
        self.fit(X)
        return self.labels_

    def _assign_clusters(self, X):
        distances = np.sqrt(((X[:, np.newaxis] - self.centroids) ** 2).sum(axis=2))
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, clusters):
        new_centroids = []
        for cluster_id in range(self.n_clusters):
            cluster_points = X[clusters == cluster_id]
            new_centroid = np.mean(cluster_points, axis=0)
            new_centroids.append(new_centroid)
        return np.array(new_centroids)
