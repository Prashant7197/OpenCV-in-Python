import cv2 as cv
img = cv.imread('img/leave.jpg')
cv.imshow('Leaf', img)
cv.waitKey(0)