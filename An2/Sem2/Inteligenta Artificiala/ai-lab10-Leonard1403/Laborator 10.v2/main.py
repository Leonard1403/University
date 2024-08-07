# Invatare supervizata(Naive Bayes) cu reprezentare Bag of Words

import pandas as pd

# 1.Încărcarea setului de date
data = pd.read_csv('reviews_mixed.csv')

# 2.Extragem caracteristicile și etichetele
X = data['Text']
y = data['Sentiment']

# 3.Transformarea textelor în reprezentarea Bag of Words
from sklearn.feature_extraction.text import CountVectorizer

# Inițializați vectorizatorul Bag of Words
vectorizer = CountVectorizer()

# Transformați textele în reprezentarea Bag of Words
X_bow = vectorizer.fit_transform(X)

# 4.Împărțirea setului de date în set de antrenare și set de testare
from sklearn.model_selection import train_test_split

# Divizați setul de date în set de antrenare și set de testare
X_train, X_test, y_train, y_test = train_test_split(X_bow, y, test_size=0.2, random_state=42)

# 5.Antrenarea unui clasificator
from sklearn.naive_bayes import MultinomialNB

# Inițializați și antrenați modelul Naive Bayes
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

# 6.Evaluarea performanțelor clasificatorului
y_pred = nb_model.predict(X_test)

# Evaluarea performanței
from sklearn.metrics import accuracy_score, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 7.Utilizarea modelului pentru predicții
example_message = "The food at this restaurant was good."
# Transformați mesajul de exemplu în reprezentarea Bag of Words
example_message_bow = vectorizer.transform([example_message])

# Obțineți predicția modelului pentru mesajul de exemplu
prediction = nb_model.predict(example_message_bow)[0]

print("Exemplu de mesaj:", example_message)
print("Predicție:", prediction)


example_message = "The bathroom wasn't clean."
# Transformați mesajul de exemplu în reprezentarea Bag of Words
example_message_bow = vectorizer.transform([example_message])

# Obțineți predicția modelului pentru mesajul de exemplu
prediction = nb_model.predict(example_message_bow)[0]

print("Exemplu de mesaj:", example_message)
print("Predicție:", prediction)
