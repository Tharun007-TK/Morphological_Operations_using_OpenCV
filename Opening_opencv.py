import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv2.imread(r"C:\Users\User\Pictures\Saved Pictures\Hamilton.jpeg", 0)

# binarize the image
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# invert the image
invert = cv2.bitwise_not(binr)

# print the inverted image
plt.imshow(invert, cmap='gray')
plt.show()


# define the kernel
kernel = np.ones((5, 5), np.uint8)

# opening the image
opening = cv2.morphologyEx(invert, cv2.MORPH_OPEN, kernel, iterations=1)

# print the opened image
plt.imshow(opening, cmap='gray')
plt.show()
