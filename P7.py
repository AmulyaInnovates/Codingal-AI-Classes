import cv2

image = cv2.imread("download.jpg")

print("Original:", image.shape, image.dtype)

small = cv2.resize(image, (200, 200))
medium = cv2.resize(image, (500, 500))
large = cv2.resize(image, (800, 800))

print("Small:", small.shape, small.dtype)
print("Medium:", medium.shape, medium.dtype)
print("Large:", large.shape, large.dtype)

cv2.imshow("Small Image", small)
cv2.imshow("Medium Image", medium)
cv2.imshow("Large Image", large)

key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite("small.jpg", small)
    cv2.imwrite("medium.jpg", medium)
    cv2.imwrite("large.jpg", large)

cv2.destroyAllWindows()