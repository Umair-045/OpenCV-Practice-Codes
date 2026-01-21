import cv2

image = cv2.imread('python.png')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Image Showing',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

save = cv2.imwrite('Gray Scale.png',gray)
print('Saved',save)


