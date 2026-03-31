import cv2
import matplotlib.pyplot as plt

image = cv2.imread("download.jpg")

image_rgb= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(image_rgb)
plt.title('RGB Image')
plt.show()

plt.imshow(image_gray, cmap='gray')
plt.title('Grayscale Image')
plt.show()

cropped_image= image_gray[100:300, 200:400]
plt.imshow(cropped_image, cmap='gray')
plt.title('Cropped Gray Image')
plt.show()

cropped_rgb= image_rgb[100:300, 200:400]
plt.imshow(cropped_rgb)
plt.title('Cropped RGB Image')
plt.show()