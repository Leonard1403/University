import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score

# citim datele din fisier
data = pd.read_csv('flowers.csv')

# selectam coloanele de interes
y_true = data['Type']
y_pred = data['PredictedType']

# calculam acuratețea, precizia și rapelul
accuracy = accuracy_score(y_true, y_pred)
# precision = precision_score(y_true, y_pred, average='macro')
precision = precision_score(y_true, y_pred, average=None, labels = ['Daisy','Tulip','Rose'])
# recall = recall_score(y_true, y_pred, average='macro')
recall = recall_score(y_true, y_pred, average=None, labels = ['Daisy','Tulip','Rose'])

# afișam rezultatele
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)


# Acuratețea (accuracy) reprezintă procentul de exemple clasificate corect din totalul de exemple. Se calculează astfel:
# accuracy = (numărul de exemple clasificate corect) / (numărul total de exemple)

# Precizia (precision) reprezintă procentul de exemple clasificate corect din totalul de exemple clasificate în acea clasă. Se calculează astfel:
# precision = (numărul de exemple clasificate corect în clasa i) / (numărul total de exemple clasificate în clasa i)

# Rapelul (recall) reprezintă procentul de exemple clasificate corect din totalul de exemple care aparțin acelei clase. Se calculează astfel:
# recall = (numărul de exemple clasificate corect în clasa i) / (numărul total de exemple din clasa i)

            # |  Daisy  |  Tulip  |   Rose  |
# -----------------------------------------
# Actual Daisy |    5    |    1   |    4    |
# Actual Tulip |    1    |    4   |    2    |
# Actual Rose  |    2    |    2   |    3    |

# 8/26 = 0.30

# precision(Daisy) = 5 / (5 + 1 + 4) = 0.50
# precision(Tulip) = 4 / (1 + 4 + 2) = 0.50
# precision(Rose)  = 3 / (2 + 2 + 3) = 0.33

# recall(Daisy) = 5 / (5 + 1 + 2) = 0.62
# recall(Tulip) = 4 / (1 + 4 + 2) = 0.57
# recall(Rose)  = 3 / (4 + 2 + 3) = 0.27