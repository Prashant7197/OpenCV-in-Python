import cv2 as cv
import numpy as np
blank =np.zeros((500,500,3), dtype='uint8')
#--- Color the blank
# blank[:]= 255,0,0

#------- Make a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=5)

#-----Fill using reverse and FILLED keywords
# cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=-1)
cv.rectangle(blank,(10,10),(250,250),(0,255,0), thickness=cv.FILLED)

cv.imshow('Blank', blank)
cv.waitKey(0)