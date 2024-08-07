import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model

# Încărcați modelul pre-antrenat pentru clasificarea emoțiilor
model = load_model('E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\\emotion_model.h5')  # Specificați calea către modelul pre-antrenat

# Directorul cu imaginile emoji
emoji_directory = 'E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data_emoji\img-apple-160'  # Specificați calea către directorul cu imagini emoji

# Directorul pentru rezultatele clasificării
output_directory = 'E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data_emoji\output'  # Specificați calea către directorul de ieșire

# Verificați și creați directorul de ieșire "unknown"
unknown_directory = os.path.join(output_directory, 'unknown')
os.makedirs(unknown_directory, exist_ok=True)

# Parcurgeți imaginile din directorul emoji
for image_name in os.listdir(emoji_directory):
    image_path = os.path.join(emoji_directory, image_name)

    # Încărcați și redimensionați imaginea
    image = load_img(image_path, target_size=(48, 48))
    image_array = img_to_array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    # Realizați predicția pentru emoția din imagine
    predictions = model.predict(image_array)[0]
    emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

    # Obțineți indicele emoției predominante
    emotion_index = np.argmax(predictions)
    predicted_emotion = emotion_labels[emotion_index]

    # Afișați rezultatul clasificării
    print(f"Imaginea {image_name} este clasificată drept: {predicted_emotion}")

    # Mutați imaginea în folderul corespunzător sau în "unknown" în funcție de rezultatul clasificării
    if predicted_emotion == 'happy' or predicted_emotion == 'surprise':
        output_folder = os.path.join(output_directory, 'happy')
    elif predicted_emotion == 'sad' or predicted_emotion == 'angry' or predicted_emotion == 'fear' or predicted_emotion == 'disgust':
        output_folder = os.path.join(output_directory, 'sad')
    else:
        output_folder = unknown_directory

    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, image_name)
    os.replace(image_path, output_path)