import cv2

image = cv2.imread('python.png')

p1 = (10,10)
p2 = (100,100)

color = (255,0,0)
thickness = 4

cv2.rectangle(image, p1,p2,color,thickness)

cv2.imshow('Rectangle Drawn',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Rectangle Drawn.png',image)