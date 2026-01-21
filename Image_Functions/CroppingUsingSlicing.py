import cv2

image = cv2.imread('python.png')

cropped = image[100:200,50:150]



cv2.imshow('Cropped Image ',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('Cropped_Image.png',cropped)