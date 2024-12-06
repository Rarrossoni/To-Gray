# Convert Packages
from PIL import Image
import numpy as np
from functions import to_grayscale, binarize
import matplotlib.pyplot as plt

# Load the image
image = Image.open('image.jpeg')  # Returns a NumPy array (H x W x 3)

# Convert image to NumPy array
image_as_list = np.array(image).tolist()

# Convert the image to gray scale
grayscale_image = to_grayscale(image_as_list)

# Convert the grayscale image to binary
binary_image = binarize(grayscale_image, threshold=128)

# Visualize all three images: original, grayscale, and binary
plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis('off')

# Grayscale image
plt.subplot(1, 3, 2)
plt.imshow(grayscale_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')

# Binary image
plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap='gray')
plt.title("Binary Image")
plt.axis('off')

plt.tight_layout()
plt.show()