import cv2

img = cv2.imread("materials/hama.jpg")
print(img.shape)

#gry = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imwrite("materials/hama_gray.jpg",gry)

#img2 = cv2.Sobel(img,cv2.CV_32F, 1, 0, ksize = 5)
#cv2.imwrite("materials/hama_sobel.jpg",img2)

#img3 = cv2.Canny(img, 30, 200)
#img3 = 256 - img3
#cv2.imwrite("materials/hama_canny.jpg",img3)

img4  = 256 - img
cv2.imwrite("materials/hama_nega.jpg",img4)

print("write img")


