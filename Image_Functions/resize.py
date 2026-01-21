import cv2

image = cv2.imread('python.png')

resize = cv2.resize(image, (300,300))

cv2.imshow('Resized Image',resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('resized_output.png',resize)