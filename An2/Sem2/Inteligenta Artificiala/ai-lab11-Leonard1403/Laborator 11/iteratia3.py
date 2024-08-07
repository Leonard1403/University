import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Directorul de date
data_directory = 'E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data'  # Specificați calea către directorul de date

# Lista etichetelor emoțiilor
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Funcția pentru extragerea caracteristicilor imaginilor
def extract_features(image_path):
    image = cv2.imread(image_path, 0)  # Citirea imaginii în format grayscale
    resized_image = cv2.resize(image, (48, 48))  # Redimensionarea imaginii la o dimensiune fixă
    flattened_image = resized_image.flatten()  # Transformarea imaginii într-un vector unidimensional
    return flattened_image

# Liste pentru stocarea datelor de antrenare și teste
X_train = []
y_train = []
X_test = []
y_test = []

# Parcurgerea fiecărei emoții și a folderelor corespunzătoare
for emotion in emotions:
    print("Train: " + emotion)
    emotion_folder = os.path.join(data_directory, 'train', emotion)
    image_files = os.listdir(emotion_folder)
    # print(image_files)
    # Extrageți caracteristicile imaginilor și adăugați-le în lista corespunzătoare
    for image_file in image_files:
        image_path = os.path.join(emotion_folder, image_file)
        features = extract_features(image_path)
        X_train.append(features)
        y_train.append(emotions.index(emotion))

# Convertiți liste în numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train)

# Antrenarea clasificatorului
classifier = SVC()
print("Antrenarea clasificatorului...")
classifier.fit(X_train, y_train)

# Testarea clasificatorului
for emotion in emotions:
    print("Test: " + emotion)
    emotion_folder = os.path.join(data_directory, 'test', emotion)
    image_files = os.listdir(emotion_folder)

    for image_file in image_files:
        image_path = os.path.join(emotion_folder, image_file)
        features = extract_features(image_path)
        X_test.append(features)
        y_test.append(emotions.index(emotion))

X_test = np.array(X_test)
y_test = np.array(y_test)

# Efectuarea predicțiilor pe datele de test
predictions = classifier.predict(X_test)

# Calcularea acurateței clasificatorului
accuracy = accuracy_score(y_test, predictions)
print(f'Acuratețea clasificatorului: {accuracy}')
