import cv2

image = cv2.imread('python.png')



cv2.circle(image, (50,50),50,(255,0,0),-1)

cv2.imshow('Circle Drawn',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Circle Drawn.png',image)