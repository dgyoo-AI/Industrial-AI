import cv2
import numpy as np
import matplotlib.pyplot as plt

diameter = -1
sigmaCol = 0
sigmaSpa = 0


def onFiltering(idx, value):
    global diameter, sigmaCol, sigmaSpa

    if idx == 0:
        diameter = value
        print('1 diameter, sigmaCol, sigmaSpa :', diameter, sigmaCol, sigmaSpa)
    elif idx == 1:
        sigmaCol = value
        print('2 diameter, sigmaCol, sigmaSpa :', diameter, sigmaCol, sigmaSpa)
    elif idx == 2:
        sigmaSpa = value
        print('3 diameter, sigmaCol, sigmaSpa :', diameter, sigmaCol, sigmaSpa)


img = cv2.imread('../Img/Lena.png').astype(np.float32) / 255

noised = (img + 0.2 * np.random.rand(*img.shape).astype(np.float32))

noised = noised.clip(0, 1)

cv2.imshow('bilateralFilter', noised)
cv2.createTrackbar('Diameter', 'bilateralFilter', 0, 30, lambda v: onFiltering(0, v))
cv2.createTrackbar('SigmaColor', 'bilateralFilter', 0, 255, lambda v: onFiltering(1, v))
cv2.createTrackbar('SigmaSpace', 'bilateralFilter', 0, 20, lambda v: onFiltering(2, v))


while True:
    bilatFilterImg = cv2.bilateralFilter(noised, diameter, sigmaCol, sigmaSpa)
    cv2.imshow('bilateralFilter', bilatFilterImg)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()