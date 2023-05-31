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

# Define the contrast function
def contrast(image, x):
    image_array = np.array(image)
    image_array = image_array.astype(float)
    image_array = (image_array - 128) * x + 128
    image_array = np.clip(image_array, 0, 255)
    return Image.fromarray(image_array.astype(np.uint8))

# Adjust the contrast of the image
adjusted_image = contrast(image, 0.7)

# Display the adjusted image and its histogram
plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(adjusted_image, cmap='gray')
plt.axis('off')
plt.subplot(2, 1, 2)
plt.hist(np.array(adjusted_image).flatten(), bins=256, range=[0, 256], color='black')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
