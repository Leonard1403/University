import os
import cv2
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Setările pentru antrenament și validare
train_data_dir = 'E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data\\train'  # Directorul cu datele de antrenament
test_data_dir = 'E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data\\test'  # Directorul cu datele de test
img_width, img_height = 48, 48  # Dimensiunile imaginilor
batch_size = 32
epochs = 10
num_classes = 2  # Numărul de clase de emoții

# Preprocesarea datelor de antrenament și validare
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=True
)

test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

# Construirea modelului
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

# drop out
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Antrenarea modelului
model.fit(train_generator, epochs=epochs)

# Salvarea modelului
model.save('emotion_model.h5')

# Evaluarea modelului pe datele de test
loss, accuracy = model.evaluate(test_generator)
print('Test accuracy:', accuracy)
