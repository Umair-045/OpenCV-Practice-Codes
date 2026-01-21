import cv2

image = cv2.imread('python.png')

cv2.imshow('Image Showing',image)
cv2.waitKey(0)
cv2.destroyAllWindows()