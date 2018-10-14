import cv2

img = cv2.imread("materials/kirin.jpg")

img = cv2.Canny(img,200,300)
img2  = 256 - img

cv2.imwrite("materials/kirin_canny.jpg",img2)
print("write image")
#cv2.imshow("image",img2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()