import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("materials/hama.jpg",0)

#cv2.imshow("img",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

plt.imshow(img, cmap = "gray", interpolation="bicubic")
plt.xticks([]),plt.yticks([])
plt.show()
