import cv2
import numpy as np

cap = cv2.VideoCapture("project_video.mp4")

tl = [601,442]
bl = [186,663]
tr = [734,442]
br = [1114,663]
while True:
    ret,img = cap.read()

    pts1 = np.float32([tl, bl, tr, br])
    pts2 = np.float32([[0, 0], [0, 480], [320, 0], [320, 480]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    eye_img = cv2.warpPerspective(img, matrix, (320, 480))
    img_hls = cv2.cvtColor(eye_img, cv2.COLOR_BGR2HLS)
    img_hls = img_hls[:, :, 1]

    gray = cv2.cvtColor(eye_img, cv2.COLOR_BGR2GRAY)

    up = 220
    low = 195
    end = cv2.inRange(gray, low, up)

    cv2.imshow("img",img)
    cv2.imshow("eye_img", eye_img)
    cv2.imshow("img_hls", img_hls)
    cv2.imshow("end", end)

    key = cv2.waitKey(10)

    if key==27:
        break

cap.release()
cv2.destroyAllWindows()