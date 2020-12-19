import cv2
from matplotlib import pyplot as plt
import numpy as np

def openWebcam():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cv2.imshow('webcam', frame)

img = cv2.imread('C:/gitclone/python/fromlove.jpg', 0)
def openImage():
    cv2.imshow('Display Image', img)

def getSizeImage():
    (h, w, d) = img.shape
    print("width={}, height={}, depth={}".format(w, h, d))

def getValueColor():
    (B, G, R) = img[50,50]
    print("R={}, G={}, B={}".format(R, G, B))

def reSizeImage():
    (h, w) = img.shape
    r = 400.0/w 
    dim = (400, int(h * r))
    resized = cv2.resize(img, dim)
    cv2.imshow('Display Image', resized)

openWebcam()
cv2.waitKey(0)
cv2.destroyAllWindows()