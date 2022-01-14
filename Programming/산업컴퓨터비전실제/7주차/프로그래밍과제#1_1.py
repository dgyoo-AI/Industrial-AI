import cv2
import numpy as np
import matplotlib.pyplot as plt


def showhistogram(col):
    cv_img = cv2.imread('../Img/Lena.png', cv2.IMREAD_COLOR)

    cv2.imshow('original', cv_img)

    if col == 2:
        cv2.destroyAllWindows()
        cv_img[:, :, 0] = (cv_img[:, :, 0] * 0.0).clip(0, 1)
        cv_img[:, :, 2] = (cv_img[:, :, 2] * 0.0).clip(0, 1)
        cv_img[:, :, [0, 1]] = cv_img[:, :, [1, 0]]

        hist, bins = np.histogram(cv_img, 256, [0, 255])

        plt.figure(figsize=(10, 8))
        plt.subplot(221), plt.imshow(cv_img)
        plt.title('original')
        plt.subplot(222), plt.plot(hist, 'r')
        #plt.fill(hist)
        plt.title('red histogram')

        rd_gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)

        hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
        rd_equal = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        plt.subplot(223), plt.imshow(rd_equal)
        plt.title('red equalization')

        equal_hist = cv2.equalizeHist(rd_gray)
        hist, bins = np.histogram(equal_hist, 256, [0, 255])
        plt.subplot(224), plt.fill_between(range(256), hist, 0)
        plt.title('equal histogram')

    elif col == 1:
        cv2.destroyAllWindows()
        cv_img[:, :, 0] = (cv_img[:, :, 0] * 0.0).clip(0, 1)
        cv_img[:, :, 1] = (cv_img[:, :, 1] * 0.0).clip(0, 1)
        cv_img[:, :, [1, 2]] = cv_img[:, :, [2, 1]]

        hist, bins = np.histogram(cv_img, 256, [0, 255])

        plt.figure(figsize=(10, 8))

        plt.subplot(221), plt.imshow(cv_img)
        plt.title('original')
        plt.subplot(222), plt.plot(hist, 'g')
        #plt.fill(hist)
        plt.title('green histogram')

        gr_gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)

        hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
        gr_equal = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        plt.subplot(223), plt.imshow(gr_equal)
        plt.title('green equalization')

        equal_hist = cv2.equalizeHist(gr_gray)
        hist, bins = np.histogram(equal_hist, 256, [0, 255])
        plt.subplot(224), plt.fill_between(range(256), hist, 0)
        plt.title('equal histogram')

    elif col == 0:
        cv2.destroyAllWindows()
        cv_img[:, :, 1] = (cv_img[:, :, 1] * 0.0).clip(0, 1)
        cv_img[:, :, 2] = (cv_img[:, :, 2] * 0.0).clip(0, 1)
        cv_img[:, :, [0, 2]] = cv_img[:, :, [2, 0]]

        hist, bins = np.histogram(cv_img, 256, [0, 255])

        plt.figure(figsize=(10, 8))
        plt.subplot(221), plt.imshow(cv_img)
        plt.title('original')
        plt.subplot(222), plt.plot(hist, 'b')
        #plt.fill(hist)
        plt.title('blue histogram')

        bl_gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)

        hsv[..., 2] = cv2.equalizeHist(hsv[..., 2])
        bl_equal = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        plt.subplot(223), plt.imshow(bl_equal)
        plt.title('blue equalization')

        equal_hist = cv2.equalizeHist(bl_gray)
        hist, bins = np.histogram(equal_hist, 256, [0, 255])
        plt.subplot(224), plt.fill_between(range(256), hist, 0)
        plt.title('equal histogram')
    else:
        return

    plt.xlim([0, 255])
    plt.show()


while True:
    k = cv2.waitKey(1)
    color = -1

    if k == ord('b'):
        color = 0
    elif k == ord('g'):
        color = 1
    elif k == ord('r'):
        color = 2
    elif k == 27:
        break

    showhistogram(color)
