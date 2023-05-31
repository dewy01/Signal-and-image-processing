from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = Image.open("cameraman.tif")

# Display the original image and its histogram
plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.subplot(2, 1, 2)
plt.hist(np.array(image).flatten(), bins=256, range=[0, 256], color='black')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

# Define the brightness function
def brightness(image, x):
    image_array = np.array(image)
    brightened_image = np.clip(image_array + x, 0, 255).astype(np.uint8)
    return Image.fromarray(brightened_image)

# Adjust the brightness of the image
brightened_image = brightness(image, 50)

# Display the adjusted image and its histogram
plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(brightened_image, cmap='gray')
plt.axis('off')
plt.subplot(2, 1, 2)
plt.hist(np.array(brightened_image).flatten(), bins=256, range=[0, 256], color='black')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
