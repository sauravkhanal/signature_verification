'''
@saurav
takes filename of scanned paper full of signature
width and height are the size of squares 
by default margin is 5 to remove inconsistency around border area
thus if input is 200*200 then signature images are of size 190*190
!!!!!!!!!!!!the file name shouldnot have space and mustnot begin with number!!!!!!!!!!!!!!!
'''
def scan_signature(filename : str , width : int, height : int , margin = 5):
    
    import numpy as np
    import cv2
    import os
    signature_gird = cv2.imread(f'{filename}',cv2.IMREAD_GRAYSCALE)
    folder_name = filename.split(".")[0]
    rows = 7
    cols = 6
    xo,yo = (0,0)#top left corner ie: starting point
    x,y = (0,0)
    #width = int(width) #width , x
    #height = int(height) #height , y
    index = 1 #for incrementing name of image
    #margin = int(margin) #margin
    dir_made = False
    adj = 0 # in order to adjust

    for i in range(rows):
        for j in range(cols):

            cropped_image = signature_gird[y + margin - adj*i : y - margin + height + adj*i, x + margin -adj*i: x - margin + width +adj*i].copy()
            
            if os.path.isdir(f'extracted_from_{folder_name}') is False:
                os.makedirs(f'extracted_from_{folder_name}')
                dir_made = True
            cv2.imwrite(f'extracted_from_{folder_name}/sign{index}.png',cropped_image)
            x = x + width #next gird in same row
            index+=1 #increment for name

        x = xo #reset x to the leftmost border
        
        y = y + height #increment y to next row

    print("Execution completed")
    if dir_made is True:
        print(f'New directory made : extracted_from_{folder_name}')
    else:
        print(f'Directory found, files replaced : extracted_from_{folder_name}')
