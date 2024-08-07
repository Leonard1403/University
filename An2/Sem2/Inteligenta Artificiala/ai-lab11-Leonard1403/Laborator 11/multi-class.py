import os

import cv2
from deepface import DeepFace

# read image
from matplotlib import pyplot as plt

img = cv2.imread('E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data\\test\\happy\\test.jpg')

# call imshow() using plt object
plt.imshow(img[:, :, :: -1])

# display that image
plt.show()

# storing the result
result = DeepFace.analyze(img,
                          actions=['emotion'])

# print result
print(result)


img = cv2.imread('E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\\data\\test\\sad\\image2.jpg')

# call imshow() using plt object
plt.imshow(img[:, :, :: -1])

# display that image
plt.show()

# storing the result
result = DeepFace.analyze(img,
                          actions=['emotion'])

# print result
print(result)

# Define the folder path containing the test images
# test_folder = "E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data\\test"

# Define the emotions labels
# emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Initialize counters for accuracy calculation
# total_images = 0
# correct_predictions = 0

# Iterate through the images in the test folder
# for root, dirs, files in os.walk(test_folder):
#     Limit the number of images per folder to 30
    # num_images_per_folder = 30
    # num_images_processed = 0

    # true_label = os.path.basename(root)
    # print(true_label)
    # for file in files:
        # Check if the number of processed images reached the limit
        # if num_images_processed >= num_images_per_folder:
        #     break

        # print("Number: " + str(num_images_processed))
        # image_path = os.path.join(root, file)

        # Perform emotion detection using DeepFace
        # result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)

        # Check if a face is detected in the image
        # if 'emotion' in result:
            # Get the predicted emotion
            # predicted_emotion = result['emotion']

            # Get the dominant emotion label
            # dominant_emotion = max(predicted_emotion, key=predicted_emotion.get)

            # Get the true label from the image folder
            # true_label = os.path.basename(root)

            # Check if the predicted emotion matches the true label
            # if dominant_emotion == true_label:
            #     correct_predictions += 1

            # total_images += 1
            # num_images_processed += 1

# Calculate accuracy
# accuracy = correct_predictions / total_images * 100

# Print the accuracy
# print("Accuracy: {:.2f}%".format(accuracy))