import cv2 as cv
from cv2 import waitKey 

img = cv.imread('hills.webp')

cv.imshow('Wave', img)

# Converting to grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blurring image (Using Gaussian blur)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade (Using canny)
canny = cv.Canny(img, 125,175)
cv.imshow('Edge', canny)

# Dilate Image (using Edge picture output)
dilated = cv.dilate(canny, (7,7), iterations = 1)
cv.imshow('Dilated', dilated)

# Eroding Image (Using dilated image)
erode = cv.erode(dilated, (7,7), iterations = 3)
cv.imshow('Erode', erode)

# Resize 
resize = cv.resize(img, (500,500), interpolation = cv.INTER_AREA)
cv.imshow('Resized', resize)

# Cropping 
cropped = img[50:200, 200:400]
cv.imshow('Crop', cropped)


cv.waitKey(0)