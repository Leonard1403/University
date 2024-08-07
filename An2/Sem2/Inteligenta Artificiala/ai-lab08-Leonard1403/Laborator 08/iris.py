import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from LogisticRegressionCustom import LogisticRegressionCustom

# 1. Incarcam setul de date Iris si il pregatim
iris_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_df = iris_df.dropna()


# 2. Separăm setul de date în două părți - datele de antrenare și datele de testare
X = iris_df.iloc[:, :-1].values
y = iris_df.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 3. Aplicăm o scalare a datelor
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 4. Aplicăm regresia logistica pentru a antrena modelul nostru
model = LogisticRegression(multi_class = "ovr")
model.fit(X_train, y_train)

# 5. Evaluăm performanța modelului nostru pe setul de date de testare
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

w0 = model.intercept_
w1 = model.coef_[0]
w2 = model.coef_[1]
w3 = model.coef_[2]
z = len(w0)
for i in range(z):
    print("y(feat1, feat2, feat3) = " + str(w0[i]) + " + " + str(w1[i]) + " *feat1 + " + str(w2[i]) + " *feat2 + " + str(w3[i]) + " *feat3")

print("Acc(tool): ", accuracy)


model = LogisticRegressionCustom()
le = LabelEncoder()
y_train_encoded = le.fit_transform(y_train)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Acc(manual): ", accuracy)

