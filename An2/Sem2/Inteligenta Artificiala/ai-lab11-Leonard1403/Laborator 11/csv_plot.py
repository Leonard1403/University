import csv
import numpy as np
import matplotlib.pyplot as plt

def plot_image_from_pixels(pixels_line):
    pixels = np.array(pixels_line.split(' '), dtype=np.uint8)
    pixels = pixels.reshape((48, 48))

    plt.imshow(pixels, cmap='gray')
    plt.axis('off')
    plt.show()

# Numele fișierului CSV
csv_file = 'E:\Facultate\An2\Sem2\Inteligenta Artificiala\Laborator 11\data_csv\\fer2013.csv'

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        pixels_line = row['pixels']
        plot_image_from_pixels(pixels_line)
