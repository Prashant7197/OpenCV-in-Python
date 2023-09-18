import cv2 as cv
import numpy as np
blank =np.zeros((500,500,3), dtype='uint8')
#--- Color the blank
blank[:]= 255,0,0

#------- Make a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=5)

#-----Fill using reverse and FILLED keywords
cv.rectangle(blank,(0,0),(250,250),(0,255,0), thickness=-1)
cv.rectangle(blank,(10,10),(250,250),(0,255,0), thickness=cv.FILLED)

#-----To make circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,0,255), thickness=3)
# cv.imshow('Circle', blank)

#-------To draw a line
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,155,155), thickness=5)

#------- To write text on Image
cv.putText(blank, 'Hello PJ', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,255,0), 2)
cv.imshow('Blank', blank)
cv.waitKey(0)