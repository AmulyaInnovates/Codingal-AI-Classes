import cv2
import numpy as np

original = cv2.imread('download.jpg')

if original is None:
    print("Image not found")
    exit()

current = original.copy()
clone = original.copy()
cropping = False
x_start, y_start, x_end, y_end = 0, 0, 0, 0

def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    cos = abs(M[0, 0])
    sin = abs(M[0, 1])

    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]

    return cv2.warpAffine(img, M, (new_w, new_h))

def nothing(x):
    pass

def mouse_crop(event, x, y, flags, param):
    global x_start, y_start, x_end, y_end, cropping, current, clone

    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start = x, y
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE and cropping:
        temp = clone.copy()
        cv2.rectangle(temp, (x_start, y_start), (x, y), (0, 255, 0), 2)
        cv2.imshow("Editor", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        x_end, y_end = x, y
        cropping = False

        x1, y1 = min(x_start, x_end), min(y_start, y_end)
        x2, y2 = max(x_start, x_end), max(y_start, y_end)

        if x2 - x1 > 0 and y2 - y1 > 0:
            current = clone[y1:y2, x1:x2]
            clone = current.copy()

cv2.namedWindow("Editor")
cv2.setMouseCallback("Editor", mouse_crop)

cv2.createTrackbar("Brightness", "Editor", 50, 100, nothing)
cv2.createTrackbar("Contrast", "Editor", 10, 30, nothing)
cv2.createTrackbar("Rotation", "Editor", 0, 360, nothing)

while True:
    brightness = cv2.getTrackbarPos("Brightness", "Editor") - 50
    contrast = cv2.getTrackbarPos("Contrast", "Editor") / 10
    angle = cv2.getTrackbarPos("Rotation", "Editor")

    temp = clone.copy()

    temp = cv2.convertScaleAbs(temp, alpha=contrast, beta=brightness)
    temp = rotate_image(temp, angle)

    cv2.imshow("Editor", temp)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        cv2.imwrite("edited_image.jpg", temp)
        print("Saved as edited_image.jpg")

    elif key == ord('r'):
        current = original.copy()
        clone = original.copy()
        print("Reset done")

    elif key == 27:
        break

cv2.destroyAllWindows()
