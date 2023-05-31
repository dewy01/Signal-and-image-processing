from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = Image.open("cameraman.tif")

# Display the image
plt.figure()
plt.imshow(image, cmap='gray')
plt.axis('off')
plt.show()

# Convert the image to grayscale
image_gray = image.convert('L')

# Display the grayscale image
plt.figure()
plt.imshow(image_gray, cmap='gray')
plt.axis('off')
plt.show()

# Convert the grayscale image to a NumPy array
image_array = np.array(image_gray)

# Calculate and plot the histogram
histogram, bins = np.histogram(image_array.flatten(), bins=256, range=[0, 256])
plt.figure()
plt.plot(histogram, color='black')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
