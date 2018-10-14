import cv2
import numpy as np

img = cv2.imread("materials/hama.jpg")
px = img[100,100]
print(px)

blue = img[100,100,0]
print(blue)

img[100,100] = [255,255,255]
print(img[100,100])

print(img.item(10,10,2))
img.itemset((10,10,2),100)
print(img.item(10,10,2))

print(img.shape)
print(img.dtype)
print(img.size)

cut = img[180:240,230:290]
img[273:333,100:160] = cut

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

b = img[:,:,0]
r = img
r[:,:,2] = 0

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("b",b)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("r",r)
cv2.waitKey(0)
cv2.destroyAllWindows()