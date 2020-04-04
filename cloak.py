import cv2
import numpy as np
import time

print("""
||||||-------------------------------------------------------------------------||||||
                                 Let's have some fun
""")


cap = cv2.VideoCapture(0)
time.sleep(3)
background=0

# capturing the background in range of 30 
# you should have video that have some seconds 
# dedicated to background frame so that it  
# could easily save the background image 
for i in range(30):
	ret,background = cap.read()

background = np.flip(background,axis=1)


# Reading from Video from webcam
while(cap.isOpened()):
	ret, img = cap.read()

    # Reverse the order of array elements along the specified axis, preserving the shape of array.
	img = np.flip(img,axis=1)

    # Using cv2.cvtColor() method 
    # Using cv2.COLOR_BGR2HSV color space conversion code 
	# convert the image - BGR to HSV 
    # as we focused on detection of red color  
  
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	value = (35, 35)

	# Apply guassian blur on src image
	blurred = cv2.GaussianBlur(hsv, value,0)

     #-------------------------------------BLOCK----------------------------# 
    # ranges should be carefully chosen 
    # setting the lower and upper range for mask1 
	lower_red = np.array([0,120,70])
	upper_red = np.array([10,255,255])

    # mask of red_color_1
	mask1 = cv2.inRange(hsv,lower_red,upper_red)
    
	# setting the lower and upper range for mask2  
	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
    
	# mask of red_color_2
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	#----------------------------------------------------------------------# 
    
	
	# the above block of code could be replaced with 
    # some other code depending upon the color of your cloth  

	# final mask
	mask = mask1+mask2

	# conducting opening morphological operation in order to
	# open up the gap between the objects connected by thin protrusions
	# that are of size less than that of the structuring element.
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5,5),np.uint8))
	
	img[np.where(mask==255)] = background[np.where(mask==255)]
	cv2.imshow('Display',img)
	k = cv2.waitKey(10)
	if k == 27:
		break

