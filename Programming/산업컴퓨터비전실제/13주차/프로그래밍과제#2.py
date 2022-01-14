import cv2
import numpy as np


imgbt1 = cv2.imread('../Img/stitching/boat1.jpg', cv2.IMREAD_COLOR)
imgbt2 = cv2.imread('../Img/stitching/boat2.jpg', cv2.IMREAD_COLOR)
imgbd1 = cv2.imread('../Img/stitching/budapest1.jpg', cv2.IMREAD_COLOR)
imgbd2 = cv2.imread('../Img/stitching/budapest2.jpg', cv2.IMREAD_COLOR)
imgnp1 = cv2.imread('../Img/stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
imgnp2 = cv2.imread('../Img/stitching/newspaper2.jpg', cv2.IMREAD_COLOR)
imgs1 = cv2.imread('../Img/stitching/s1.jpg', cv2.IMREAD_COLOR)
imgs2 = cv2.imread('../Img/stitching/s2.jpg', cv2.IMREAD_COLOR)

imgbt1 = cv2.resize(imgbt1, dsize=(640, 480))
imgbt2 = cv2.resize(imgbt2, dsize=(640, 480))
imgs_list1 = [imgbt1, imgbt2]

imgbd1 = cv2.resize(imgbd1, dsize=(640, 480))
imgbd2 = cv2.resize(imgbd2, dsize=(640, 480))
imgs_list2 = [imgbd1, imgbd2]

imgnp1 = cv2.rotate(imgnp1, cv2.ROTATE_90_COUNTERCLOCKWISE)
imgnp2 = cv2.rotate(imgnp2, cv2.ROTATE_90_COUNTERCLOCKWISE)
imgnp1 = cv2.resize(imgnp1, dsize=(640, 480))
imgnp2 = cv2.resize(imgnp2, dsize=(640, 480))
imgs_list3 = [imgnp1, imgnp2]

imgs1 = cv2.resize(imgs1, dsize=(640, 480))
imgs2 = cv2.resize(imgs2, dsize=(640, 480))
imgs_list4 = [imgs1, imgs2]

imgs_SIFT1 = imgs_list1.copy()
imgs_SIFT2 = imgs_list2.copy()
imgs_SIFT3 = imgs_list3.copy()
imgs_SIFT4 = imgs_list4.copy()

detector = cv2.xfeatures2d.SIFT_create(50)

for i in range(len(imgs_SIFT1)):
    kpnts, dscrs = detector.detectAndCompute(imgs_SIFT1[i], None)
    imgs_SIFT1[i] = cv2.drawKeypoints(imgs_SIFT1[i], kpnts, None, (0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for i in range(len(imgs_SIFT2)):
    kpnts, dscrs = detector.detectAndCompute(imgs_SIFT2[i], None)
    imgs_SIFT2[i] = cv2.drawKeypoints(imgs_SIFT2[i], kpnts, None, (0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for i in range(len(imgs_SIFT3)):
    kpnts, dscrs = detector.detectAndCompute(imgs_SIFT3[i], None)
    imgs_SIFT3[i] = cv2.drawKeypoints(imgs_SIFT3[i], kpnts, None, (0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for i in range(len(imgs_SIFT4)):
    kpnts, dscrs = detector.detectAndCompute(imgs_SIFT4[i], None)
    imgs_SIFT4[i] = cv2.drawKeypoints(imgs_SIFT4[i], kpnts, None, (0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SIFT1 keypoints', np.hstack(imgs_SIFT1))
cv2.imshow('SIFT2 keypoints', np.hstack(imgs_SIFT2))
cv2.imshow('SIFT3 keypoints', np.hstack(imgs_SIFT3))
cv2.imshow('SIFT4 keypoints', np.hstack(imgs_SIFT4))

cv2.waitKey()
cv2.destroyAllWindows()


imgs_SURF1 = imgs_list1.copy()
imgs_SURF2 = imgs_list2.copy()
imgs_SURF3 = imgs_list3.copy()
imgs_SURF4 = imgs_list4.copy()

surf = cv2.xfeatures2d.SURF_create(10000)
surf.setExtended(True)
surf.setNOctaves(3)
surf.setNOctaveLayers(10)
surf.setUpright(False)

for i in range(len(imgs_SURF1)):
    kpnts, dscrs = surf.detectAndCompute(imgs_SURF1[i], None)
    imgs_SURF1[i] = cv2.drawKeypoints(imgs_SURF1[i], kpnts, None, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for i in range(len(imgs_SURF2)):
    kpnts, dscrs = surf.detectAndCompute(imgs_SURF2[i], None)
    imgs_SURF2[i] = cv2.drawKeypoints(imgs_SURF2[i], kpnts, None, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for i in range(len(imgs_SURF3)):
    kpnts, dscrs = surf.detectAndCompute(imgs_SURF3[i], None)
    imgs_SURF3[i] = cv2.drawKeypoints(imgs_SURF3[i], kpnts, None, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

for i in range(len(imgs_SURF4)):
    kpnts, dscrs = surf.detectAndCompute(imgs_SURF4[i], None)
    imgs_SURF4[i] = cv2.drawKeypoints(imgs_SURF4[i], kpnts, None, (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('SURF1 descriptors', np.hstack(imgs_SURF1))
cv2.imshow('SURF2 descriptors', np.hstack(imgs_SURF2))
cv2.imshow('SURF3 descriptors', np.hstack(imgs_SURF3))
cv2.imshow('SURF4 descriptors', np.hstack(imgs_SURF4))

cv2.waitKey()
cv2.destroyAllWindows()


imgs_ORB1 = imgs_list1.copy()
imgs_ORB2 = imgs_list2.copy()
imgs_ORB3 = imgs_list3.copy()
imgs_ORB4 = imgs_list4.copy()

orb = cv2.ORB_create(100)

kpnts1, dscrs1 = orb.detectAndCompute(cv2.cvtColor(imgs_ORB1[0], cv2.COLOR_BGR2GRAY), None)
kpnts2, dscrs2 = orb.detectAndCompute(cv2.cvtColor(imgs_ORB1[1], cv2.COLOR_BGR2GRAY), None)
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(dscrs1, dscrs2)

pts1 = np.float32([kpnts1[m.queryIdx].pt for m in matches]).reshape(-1, 2)
pts2 = np.float32([kpnts1[m.trainIdx].pt for m in matches]).reshape(-1, 2)
H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 1.0)   # Matching Point 를 작게 설정할 수록 정확한 Point 만 매칭 시킴

matImg = cv2.drawMatches(imgs_ORB1[0], kpnts1, imgs_ORB1[1], kpnts2, [m for i, m in enumerate(matches) if mask[i]], None)

cv2.imshow('ORB Homography1', matImg)

kpnts1, dscrs1 = orb.detectAndCompute(cv2.cvtColor(imgs_ORB2[0], cv2.COLOR_BGR2GRAY), None)
kpnts2, dscrs2 = orb.detectAndCompute(cv2.cvtColor(imgs_ORB2[1], cv2.COLOR_BGR2GRAY), None)
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(dscrs1, dscrs2)

pts1 = np.float32([kpnts1[m.queryIdx].pt for m in matches]).reshape(-1, 2)
pts2 = np.float32([kpnts1[m.trainIdx].pt for m in matches]).reshape(-1, 2)
H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 1.0)   # Matching Point 를 작게 설정할 수록 정확한 Point 만 매칭 시킴

matImg = cv2.drawMatches(imgs_ORB2[0], kpnts1, imgs_ORB2[1], kpnts2, [m for i, m in enumerate(matches) if mask[i]], None)

cv2.imshow('ORB Homography2', matImg)

kpnts1, dscrs1 = orb.detectAndCompute(cv2.cvtColor(imgs_ORB3[0], cv2.COLOR_BGR2GRAY), None)
kpnts2, dscrs2 = orb.detectAndCompute(cv2.cvtColor(imgs_ORB3[1], cv2.COLOR_BGR2GRAY), None)
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(dscrs1, dscrs2)

pts1 = np.float32([kpnts1[m.queryIdx].pt for m in matches]).reshape(-1, 2)
pts2 = np.float32([kpnts1[m.trainIdx].pt for m in matches]).reshape(-1, 2)
H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 1.0)   # Matching Point 를 작게 설정할 수록 정확한 Point 만 매칭 시킴

matImg = cv2.drawMatches(imgs_ORB3[0], kpnts1, imgs_ORB3[1], kpnts2, [m for i, m in enumerate(matches) if mask[i]], None)

cv2.imshow('ORB Homography3', matImg)

kpnts1, dscrs1 = orb.detectAndCompute(cv2.cvtColor(imgs_ORB4[0], cv2.COLOR_BGR2GRAY), None)
kpnts2, dscrs2 = orb.detectAndCompute(cv2.cvtColor(imgs_ORB4[1], cv2.COLOR_BGR2GRAY), None)
matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(dscrs1, dscrs2)

pts1 = np.float32([kpnts1[m.queryIdx].pt for m in matches]).reshape(-1, 2)
pts2 = np.float32([kpnts1[m.trainIdx].pt for m in matches]).reshape(-1, 2)
H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 1.0)   # Matching Point 를 작게 설정할 수록 정확한 Point 만 매칭 시킴

matImg = cv2.drawMatches(imgs_ORB4[0], kpnts1, imgs_ORB4[1], kpnts2, [m for i, m in enumerate(matches) if mask[i]], None)

cv2.imshow('ORB Homography4', matImg)

cv2.waitKey()
cv2.destroyAllWindows()
