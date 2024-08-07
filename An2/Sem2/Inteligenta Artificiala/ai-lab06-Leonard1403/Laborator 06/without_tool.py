import csv
import matplotlib.pyplot as plt

# Load data
with open('data/v1_world-happiness-report-2017.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    X = []
    y = []
    for row in reader:
        X.append([float(row[1]), float(row[5])])
        y.append(float(row[2]))

# Split data into train and test sets
n = len(X)
n_train = int(n * 0.8)
X_train, X_test = X[:n_train], X[n_train:]
y_train, y_test = y[:n_train], y[n_train:]

# Compute model parameters
def linear_regression(X, y):
    n = len(X)
    sum_x1 = sum_x2 = sum_y = sum_x1_sq = sum_x2_sq = sum_x1x2 = sum_x1y = sum_x2y = 0
    for i in range(n):
        x1, x2 = X[i]
        sum_x1 += x1
        sum_x2 += x2
        sum_y += y[i]
        sum_x1_sq += x1**2
        sum_x2_sq += x2**2
        sum_x1x2 += x1 * x2
        sum_x1y += x1 * y[i]
        sum_x2y += x2 * y[i]

    denominator = n * sum_x1_sq - sum_x1**2 + n * sum_x2_sq - sum_x2**2
    w1 = (n * sum_x1x2 - sum_x1 * sum_x2) / denominator
    w2 = (sum_x2_sq * sum_y - sum_x2 * sum_x1y + sum_x1_sq * sum_y - sum_x1 * sum_x2y) / denominator
    w0 = sum_y / n - w1 * sum_x1 / n - w2 * sum_x2 / n

    return w0, w1, w2
w0, w1, w2 = linear_regression(X_train, y_train)

print('f(x) = ', w2, ' * x^2 + ', w1, ' * x + ', w0)

# Compute predictions and MSE on test set
y_pred = []
for i in range(n - n_train):
    x1, x2 = X_test[i]
    y_pred.append(w0 + w1 * x1 + w2 * x2)
mse = sum((y_test[i] - y_pred[i])**2 for i in range(n - n_train)) / (n - n_train)
print('Validation MSE:', mse)

# Visualize the data and the model
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = [row[0] for row in X_train]
ys = [row[1] for row in X_train]
zs = y_train
ax.scatter(xs, ys, zs, c='r', marker='o')
ax.set_xlabel('GDP per capita')
ax.set_ylabel('Freedom')
ax.set_zlabel('Happiness')

x_surf, y_surf = [], []
for x in range(100):
    x_val = xs[0] + x / 100 * (xs[-1] - xs[0])
    for y in range(100):
        y_val = ys[0] + y / 100 * (ys[-1] - ys[0])
        x_surf.append(x_val)
        y_surf.append(y_val)
        z_surf = []
for i in range(len(x_surf)):
    z_surf.append(w0 + w1 * x_surf[i] + w2 * y_surf[i])
ax.plot_trisurf(x_surf, y_surf, z_surf, cmap='coolwarm')
plt.show()
