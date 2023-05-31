import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
I = cv2.imread('testfoto.jpg')

# Display the original image
plt.figure()
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Apply image filtering
ww = 5
kernel1 = np.ones((ww, ww)) / ww**2
b_img = cv2.filter2D(I, -1, kernel1)
plt.figure()
plt.imshow(cv2.cvtColor(b_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Apply custom kernel filtering
kernel = -np.ones((8, 8))
kernel[4, 4] = -np.sum(kernel) - 1 + 8**2
kernel = kernel / np.sum(kernel)
out = cv2.filter2D(I, -1, kernel)
plt.figure()
plt.imshow(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

# Detect faces using Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(I, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with detected faces
plt.figure()
plt.imshow(cv2.cvtColor(I, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
