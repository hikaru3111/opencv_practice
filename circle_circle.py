import numpy as np
import cv2

#create "seikaiha"

col_number = 16
row_number = 6

circle_r = 80
circle_number = 7
circle_color1 = (255,0,0)
circle_color2 = (255,255,255)

def center_list_maker(circle_r,col_number,row_number):
    center_list = []
    for i in range(0,col_number):
        for j in range(0,row_number):
            if i%2 ==1:
                center = (circle_r + (2 * circle_r * j),(circle_r * i)//2)
            else:
                center = (2 * circle_r *j, (circle_r*i)//2)
            center_list.append(center)
    return center_list

print(center_list_maker(circle_r,col_number,row_number))

# draw a circle
def paint_circle(img,center,circle_r,circle_color1,circle_color2,circle_number):
    count = 0
    band_width = circle_r//circle_number
    #print("band_width:" + str(band_width))
    for i in range(1,circle_number+2)[::-1]:
        r_ = band_width * i
        #print(r_)
        if count == 0:
            img = cv2.circle(img,center,r_,circle_color1,-1)
            count = 1
            #print("color1")
        elif count == 1:
            img = cv2.circle(img,center,r_,circle_color2,-1)
            count = 0
            #print("color2")

    return img


def paint_wave(circle_r,circle_color1,circle_color2,circle_number,col_number,row_number):
    img_width = 2 * circle_r * (row_number - 1)
    print("width"+ str(img_width))
    img_height = (circle_r * (col_number - 1)//2) - circle_r
    print("height" + str(img_height))
    img = np.zeros((img_height,img_width,3),np.uint8)
    center_list = center_list_maker(circle_r,col_number,row_number)
    for center in center_list:
        paint_circle(img,center,circle_r,circle_color1,circle_color2,circle_number)

    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

paint_wave(circle_r,circle_color1,circle_color2,circle_number,col_number,row_number)
