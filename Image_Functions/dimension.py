import cv2

image = cv2.imread('python.png')

h,w,c = image.shape

print(f"Image loaded : \n height :{h} \n width : {w}, \n channels : {c}")