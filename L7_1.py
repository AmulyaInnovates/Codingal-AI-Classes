import cv2 

img = cv2.imread('download.jpg')

cv2.nameWindow('Load Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Load Window', 800,500)

cv2.imshow('Load Window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()