import cv2
import numpy as np
import math
import operator

#Creates the picture
height = 1024
width = 1024
img = np.zeros((height,width,3), np.uint8)

#Adds the pictures gradiant
c = 0
i = 0
while i < width:
    for i in range(height):
        for j in range(width):
            img[i][j] = [c, c, c]
            c = c + 0.25
    i = i + 1

#Adds the static shapes on the left and right from a sample taken from image center
cshape = img[height//2-30 : height//2+30, width//2-30 : width//2+30]
img[510:570, 70:130] = cshape
img[510:570, 929:989] = cshape

#Defines the Path of the moving shape
def shape_path(t, scale, offset):
    res = (int(scale*math.cos(t)+offset), int(scale*math.sin(t*5)+offset))
    return res

timer = 0.0

while True:
    
    #Copies the image
    cimg = img.copy()
    #Draws the sampeled shape in the way of the defined path
    timer += 0.002
    pt1 = shape_path(timer, 430, 500)
    size = (60, 60)
    pt2 = tuple(map(operator.add, pt1, size))
    cimg[pt1[1]:pt2[1], pt1[0]:pt2[0]] = cshape

    #Shows the Picture and Animation in a Window
    title = "Optical Illusion"
    cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
    cv2.imshow(title, cimg)
     
    #Closes the window with "q"
    if cv2.waitKey(10) == ord("q"):
        break

cv2.destroyAllWindows()