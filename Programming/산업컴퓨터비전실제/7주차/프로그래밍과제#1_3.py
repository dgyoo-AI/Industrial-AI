import cv2
import numpy as np
import matplotlib.pyplot as plt


def showfilterimg(mode):
    image = cv2.imread('../Img/Lena.png', 0).astype(np.float32) / 255

    cv2.imshow("original", image)

    if mode == 0:
        hft = np.fft.fft2(image)
        hft_shift = np.fft.fftshift(hft)
        hft_shift[image.shape[0]//2-30:image.shape[0]//2+30, image.shape[1]//2-30:image.shape[0]//2+30] = 0
        hft_ishift = np.fft.ifftshift(hft_shift)
        result_img = np.fft.ifft2(hft_ishift)
        result_img = np.abs(result_img)

        plt.figure(figsize=(10, 6))
        plt.subplot(121)
        plt.title('original')
        plt.imshow(image, cmap='gray')
        plt.subplot(122)
        plt.title('DFT')
        plt.imshow(result_img, cmap='gray')

    elif mode == 1:

        cv2.destroyAllWindows()

        fft = cv2.dft(image, flags=cv2.DFT_COMPLEX_OUTPUT)

        sz = int(input("Circle radius : "))

        mask = np.zeros(fft.shape, np.uint8)
        cv2.circle(mask, (250, 250), sz*2, (255, 255, 255), -1)

        fft_shift = np.fft.fftshift(fft, axes=[0, 1])
        fft_shift *= mask
        fft = np.fft.ifftshift(fft_shift, axes=[0, 1])
        filtered = cv2.idft(fft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)

        # mask_new = np.dstack((mask, np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)))
        #
        plt.figure(figsize=(10, 6))
        plt.subplot(121)
        plt.title('original')
        plt.imshow(image, cmap='gray')
        plt.subplot(122)
        plt.title('DFT')
        plt.imshow(filtered, cmap='gray')

    else:
        return

    plt.tight_layout(True)
    plt.show()


while True:
    k = cv2.waitKey(1)
    pf = -1

    if k == ord('h'):
        pf = 0
    elif k == ord('l'):
        pf = 1
    elif k == 27:
        break

    showfilterimg(pf)
