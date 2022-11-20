import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("test_images/test5.jpg")

tl = [601,442]
bl = [186,663]
tr = [734,442]
br = [1114,663]

pts1 = np.float32([tl,bl,tr,br])
pts2 = np.float32([[0,0],[0,480],[320,0],[320,480]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
eye_img = cv2.warpPerspective(img,matrix,(320,480))

img_hls = cv2.cvtColor(eye_img,cv2.COLOR_BGR2HLS)


binary_output = np.zeros_like(img_hls[:,:,1])

img_hls = img_hls[:, :, 1]

gray = cv2.cvtColor(eye_img,cv2.COLOR_BGR2GRAY)

up = 220
low = 195
end = cv2.inRange(gray,low,up)
plt.imshow(end)
plt.show()



cv2.waitKey(0)
