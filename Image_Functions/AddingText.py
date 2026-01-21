import cv2

image = cv2.imread('python.png')



cv2.putText(image, "Hello OpenCV",(10,70),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,255,255),2)

cv2.imshow('Add Text',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Adding Text.png',image)