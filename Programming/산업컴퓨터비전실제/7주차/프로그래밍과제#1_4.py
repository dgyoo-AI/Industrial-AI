import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('../Img/Lena.png', 0)


def showResult(mf):

    _, binary = cv2.threshold(image, -1, 1, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    if mf == 0:
        cv2.destroyAllWindows()
        count = input("Erosion Count : ")
        eroded = cv2.morphologyEx(binary, cv2.MORPH_ERODE, (3, 3), iterations=int(count))

        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.title('binary')
        plt.imshow(binary, cmap='gray')
        plt.subplot(122)
        plt.title(str("Erosion count : {}".format(int(count))))
        plt.imshow(eroded, cmap='gray')

    elif mf == 1:
        cv2.destroyAllWindows()
        count = input("Dilation Count : ")
        dilated = cv2.morphologyEx(binary, cv2.MORPH_DILATE, (3, 3), iterations=int(count))

        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.title('binary')
        plt.imshow(binary, cmap='gray')
        plt.subplot(122)
        plt.title(str("Dilation count : {}".format(int(count))))
        plt.imshow(dilated, cmap='gray')

    elif mf == 2:
        cv2.destroyAllWindows()
        count = input("Opening Count : ")
        opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=int(count))

        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.title('binary')
        plt.imshow(binary, cmap='gray')
        plt.subplot(122)
        plt.title(str("Opening count : {}".format(int(count))))
        plt.imshow(opened, cmap='gray')

    elif mf == 3:
        cv2.destroyAllWindows()
        count = input("Closing Count : ")
        closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)), iterations=int(count))

        plt.figure(figsize=(10, 5))
        plt.subplot(121)
        plt.title('binary')
        plt.imshow(binary, cmap='gray')
        plt.subplot(122)
        plt.title(str("Closing count : {}".format(int(count))))
        plt.imshow(closed, cmap='gray')
    else:
        return

    plt.tight_layout(True)
    plt.show()


while True:

    cv2.imshow('original', image)
    k = cv2.waitKey(1)
    mfType = -1

    if k == ord('e'):
        mfType = 0
    elif k == ord('d'):
        mfType = 1
    elif k == ord('o'):
        mfType = 2
    elif k == ord('c'):
        mfType = 3
    elif k == 27:
        break

    showResult(mfType)
