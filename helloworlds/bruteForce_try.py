import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img=cv2.imread('image.jpg',0)
tem=cv2.imread('template.jpg',0)

# descriptors (differs in distance measurements)
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img,None)
kp2, des2 = orb.detectAndCompute(tem,None)

# create BFMatcher object, crosscheck is for better results
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)


# Match descriptors.
matches = bf.match(des1,des2)
# bf.match returns a list of DMatch objects, whose one of the attributes is distance, the lower it is, the better it is.


# Sort them by the distance attribute.
matches = sorted(matches, key = lambda x:x.distance) # best matches have low distance

'''
DMatch.distance - Distance between descriptors. The lower, the better it is.
DMatch.trainIdx - Index of the descriptor in train descriptors
DMatch.queryIdx - Index of the descriptor in query descriptors
DMatch.imgIdx - Index of the train image.
'''

img_output = cv2.drawMatches(img,kp1,tem,kp2,matches, None ,flags=2)

plt.imshow(img_output)
plt.show()

cv2.imshow('img',img_output)

k = cv2.waitKey(0) & 0xFF

if k == 27 or k == ord('q'):   # esc key
	cv2.destroyAllWindows()
elif k == ord('s'):    # press 's' to save
	cv2.imwrite('output.png', img_output)
	cv2.destroyAllWindows()
else:
	print("this key does nothing!")

