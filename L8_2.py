import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('download.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

angle = 45
scale = 1.0

M = cv2.getRotationMatrix2D(center, angle, scale)

cos = abs(M[0, 0])
sin = abs(M[0, 1])

new_w = int((h * sin) + (w * cos))
new_h = int((h * cos) + (w * sin))

M[0, 2] += (new_w / 2) - center[0]
M[1, 2] += (new_h / 2) - center[1]

rotated = cv2.warpAffine(image, M, (new_w, new_h))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.axis('off')
plt.show()

alpha = 1.5
beta = 0

contrast = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

contrast_rgb = cv2.cvtColor(contrast, cv2.COLOR_BGR2RGB)
plt.imshow(contrast_rgb)
plt.title("High Contrast Image")
plt.axis('off')
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image, brightness_matrix)

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter_rgb)
plt.title("Brighter Image")
plt.axis('off')
plt.show()
