import cv2
import numpy as np

img1 = cv2.imread('../Img/stitching/boat1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('../Img/stitching/budapest1.jpg', cv2.IMREAD_COLOR)
img3 = cv2.imread('../Img/stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
img4 = cv2.imread('../Img/stitching/s1.jpg', cv2.IMREAD_COLOR)

img1 = cv2.resize(img1, dsize=(640, 480))
img2 = cv2.resize(img2, dsize=(640, 480))
img3 = cv2.rotate(img3, cv2.ROTATE_90_COUNTERCLOCKWISE)
img3 = cv2.resize(img3, dsize=(640, 480))
img4 = cv2.resize(img4, dsize=(640, 480))

imgOrg = [img1, img2, img3, img4]
imgLine = []
imgCanny = []
for i in range(len(imgOrg)):
    imgCanny.append(imgOrg[i].copy())


for i in range(len(imgOrg)):
    imgLine.append(cv2.Canny(imgCanny[i], 150, 250))

    counts, new = cv2.findContours(imgLine[i], cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    cv2.drawContours(imgCanny[i], counts, -1, (0, 255, 0), 1)


corners = []
imgCorner = []

for i in range(len(imgOrg)):
    corners.append(cv2.cornerHarris(cv2.cvtColor(imgOrg[i], cv2.COLOR_BGR2GRAY), 2, 3, 0.04))
    corners[i] = cv2.dilate(corners[i], None)

    imgCorner.append(np.copy(imgOrg[i]))
    lineDraw = imgCorner[i]
    lineDraw[corners[i]>0.1*corners[i].max()] = [0, 255, 0]
    imgCorner[i] = lineDraw

    imgCorner[i] = np.hstack((imgCorner[i], imgCanny[i]))
    if i % 2 == 1:
        imgCorner[i-1] = np.vstack((imgCorner[i-1], imgCorner[i]))


cv2.imshow('Harris corner & Canny Edge1', imgCorner[0])
cv2.imshow('Harris corner & Canny Edgy2', imgCorner[2])
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
