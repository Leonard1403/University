import os

import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Încarcă modelul salvat
model = load_model('emotion_model.h5')

# Definirea claselor de emoții
emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Funcția pentru a face predicția emoției pe baza unei imagini
def predict_emotion(image):
    # Redimensionarea imaginii pentru a o potrivi cu dimensiunile acceptate de model și a converti la 3 canale de culoare
    resized_image = cv2.resize(image, (48, 48))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)
    image = np.reshape(rgb_image, (1, 48, 48, 3))
    image = image / 255.0

    # Realizarea predicției
    emotion_probabilities = model.predict(image)
    # print(emotion_probabilities)
    emotion_index = np.argmax(emotion_probabilities)
    emotion_label = emotion_labels[emotion_index]
    return emotion_label

test_data_dir = 'E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data\\test'

# Preia lista de fișiere din directorul de test pentru fiecare clasă de emoție
emotions = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
total_samples = 0
correct_predictions = 0

# for emotion in emotions:
#     emotion_dir = os.path.join(test_data_dir, emotion)
#     image_files = os.listdir(emotion_dir)
#
#     image_files = image_files[:40]  # elimină această linie dacă vrei să testezi pe toate imaginile
#     for image_file in image_files:
#         image_path = os.path.join(emotion_dir, image_file)
#         image = cv2.imread(image_path)
#
#         Realizarea predicției emoției
        # predicted_emotion = predict_emotion(image)
        #
        # Verificarea corectitudinii predicției
        # if predicted_emotion == emotion:
        #     correct_predictions += 1
        #
        # total_samples += 1

# Calcularea acurateței
# accuracy = correct_predictions / total_samples

# Afișarea acurateței
# print("Acuratețe:", accuracy)


# Încărcarea imaginii pentru predicție
image_path = 'E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data\\test\happy\\test.jpg'  # înlocuiește 'path_to_image.jpg' cu calea către fișierul imaginii
image = cv2.imread(image_path)

# Realizarea predicției emoției
emotion = predict_emotion(image)

# Afișarea emoției prezise
print("Emotion:", emotion)
