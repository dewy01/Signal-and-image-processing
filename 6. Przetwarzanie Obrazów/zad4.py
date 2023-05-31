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

# Define the binaryzacja function
def binaryzacja(image, bp):
    image_array = np.array(image)
    image_array[image_array > bp] = 255
    image_array[image_array <= bp] = 0
    return Image.fromarray(image_array.astype(np.uint8))

# Apply binaryzacja to the image
binary_image = binaryzacja(image, 127)

# Display the binary image and its histogram
plt.figure()
plt.subplot(2, 1, 1)
plt.imshow(binary_image, cmap='gray')
plt.axis('off')
plt.subplot(2, 1, 2)
plt.hist(np.array(binary_image).flatten(), bins=2, range=[0, 256], color='black')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
