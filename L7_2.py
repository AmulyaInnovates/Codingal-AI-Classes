import cv2

img = cv2.imread('download.jpg')

cv2.namedWindow('Load Window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Load Window', 224, 224)

gray_img = cv2.cvtColor(img, cv2.BGR2GRAY)

cv2.imshow('Load Window', gray_img)

key= cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('gray_scale_resized_image.jpg', gray_img)
    
else:
    print("Image not saved")
    
cv2.destroyAllWindows()