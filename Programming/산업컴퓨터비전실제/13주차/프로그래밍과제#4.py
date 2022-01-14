import cv2
import numpy as np

img1 = cv2.imread('../Img/stitching/dog_a.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('../Img/stitching/dog_b.jpg', cv2.IMREAD_COLOR)

img1 = cv2.resize(img1, dsize=(1024, 768))
img2 = cv2.resize(img2, dsize=(1024, 768))
img_list = [img1, img2]

prev_pts = None
prev_gray_frame = None
tracks = None
idx = 0

while True:
    if len(img_list)-1 < idx:
        idx = 0

    frame = img_list[idx].copy()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if prev_pts is not None:
        pts, status, errors = cv2.calcOpticalFlowPyrLK(prev_gray_frame, gray_frame, prev_pts, None, winSize=(15, 15),
                                                       maxLevel=5, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))    # Tracking 이 종료되는 지점 설정
        good_pts = pts[status == 1]
        if tracks is None:
            tracks = good_pts
        else:
            tracks = np.vstack((tracks, good_pts))
        for p in tracks:
            cv2.circle(frame, (p[0], p[1]), 3, (0, 255, 0), -1)
    else:
        pts = cv2.goodFeaturesToTrack(gray_frame, 500, 0.05, 10)
        pts = pts.reshape(-1, 1, 2)

    idx += 1

    prev_pts = pts
    prev_gray_frame = gray_frame

    cv2.imshow('Pyramid Lucas-Kanade', frame)
    key = cv2.waitKey() & 0xff
    if key == 27:
        break
    if key == ord('c'):
        tracks = None
        prev_pts = None
        idx = 0

cv2.destroyAllWindows()


def display_flow(img, flow, stride=50):
    for index in np.ndindex(flow[::stride, ::stride].shape[:2]):
        pt1 = tuple(i*stride for i in index)
        delta = flow[pt1].astype (np. int32)[::-1]
        pt2 = tuple(pt1 + 10*delta)
        if 2 <= cv2.norm(delta) <= 10:
            cv2.arrowedLine(img, pt1[::-1], pt2[::-1], (0, 0, 255), 2, cv2.LINE_AA, 0, 0.2)


prev = None
count = 0

while True:
    if len(img_list) - 1 < count:
        count = 0

    frame = img_list[count].copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if prev is None:
        prev = gray
    else:
        flow = cv2.calcOpticalFlowFarneback(prev, gray, flow=None,
                                            pyr_scale=0.7, levels=3, winsize=50, iterations=3,
                                            poly_n=5, poly_sigma=1.1,
                                            flags=cv2.OPTFLOW_FARNEBACK_GAUSSIAN)
        display_flow(frame, flow)
        prev = gray

    cv2.imshow('Gunner Farneback', frame)
    count += 1
    key = cv2.waitKey() & 0xFF
    if key == 27:
        break
    if key == ord('c'):
        break

cv2.destroyAllWindows()


prev_frame = cv2.cvtColor(img_list[0], cv2.COLOR_BGR2GRAY)
flow_DualTVL1 = cv2.createOptFlow_DualTVL1()
count = 0

while True:
    if len(img_list) - 1 < count:
        count = 0

    frame = img_list[count].copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if not flow_DualTVL1.getUseInitialFlow():
        opt_flow = flow_DualTVL1.calc(prev_frame, gray, None)
        flow_DualTVL1.setUseInitialFlow(True)
    else:
        opt_flow = flow_DualTVL1.calc(prev_frame, gray, opt_flow)

    display_flow(frame, opt_flow)

    cv2.imshow('Dual TVL1', frame)
    prev_frame = gray.copy()
    count += 1
    key = cv2.waitKey() & 0xFF
    if key == 27:
        break
    if key == ord('c'):
        break

cv2.destroyAllWindows()
