import cv2
import tensorflow.python.keras.models
from tensorflow.keras.models import load_model
import numpy as np

# Încarcă modelul pre-antrenat pentru recunoașterea emoțiilor

model = load_model('E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\model\\fer.h5')  # înlocuiește 'path_to_model.h5' cu calea către fișierul .h5 al modelului
