import cv2

image = cv2.imread('python.png')

h,w = image.shape[:2]
center = (w//2,h//2)

M = cv2.getRotationMatrix2D(center , 90 , 1.0)
rotated_image = cv2.warpAffine(image,M,(w,h))


cv2.imshow("Original Image",image)
cv2.imshow("Rotated",rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Rotated_Image.png',rotated_image)