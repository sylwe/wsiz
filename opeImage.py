#import th necessary packages
import cv2
import argparse

#load imge from disk via "cv2.imread" and then grab the spatial
#dimension, inc. width, height, and number of channels

img = cv2.imread('WOT32488.jpg',0)
image = img = cv2.imread('WOT32488.jpg')

(h, w, c) = image.shape[:3]

# display the image width, height, and number of channels to our
# terminal
print("width: {} pixels".format(w))
print("height: {}  pixels".format(h))
print("channels: {}".format(c))

# show the image and wait for a keypress
cv2.imshow('image',img)
cv2.waitKey(0)

