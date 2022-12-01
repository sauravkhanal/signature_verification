'''
@saurav
takes filename of scanned paper full of signature
width and height are the size of squares 
by default margin is 5 to remove inconsistency around border area
thus if input is 200*200 then signature images are of size 190*190
!!!!!!!!!!!!the file name shouldnot have space and mustnot begin with number!!!!!!!!!!!!!!!
'''

import numpy as np
import cv2
import os

filepath  = input("enter file path as(A:/test/imagee1.png): ")
folder_name = input("enter name of folder to save the images eg(A:/test/ectracted_images): ")
if os.path.isdir(f'{folder_name}') is False:
    os.makedirs(f'{folder_name}')
    dir_made = True

signature_gird = cv2.imread(f'{filepath}',cv2.IMREAD_GRAYSCALE)
rows = 7
cols = 6
xo,yo = (0,0)#top left corner ie: starting point
x,y = (0,0)
width = 200 #width , x
height = 200 #height , y
index = 1 #for incrementing name of image
margin = 5
dir_made = False
adj = 0 # in order to adjust

for i in range(rows):
    for j in range(cols):

        cropped_image = signature_gird[y + margin  : y - margin + height , x + margin : x - margin + width ]
        
        cv2.imwrite(f'{folder_name}/sign{index}.png',cropped_image)
        x = x + width #next gird in same row
        index+=1 #increment for namea

    x = xo #reset x to the leftmost border

    y = y + height #increment y to next row

print("Execution completed")
if dir_made is True:
    print(f'New directory made : {folder_name}')
else:
    print(f'Directory found, files replaced : {folder_name}')
