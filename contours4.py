import cv2
import numpy as np

img = cv2.imread('images/th.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY_INV)
#cv2.imwrite('thresh.jpg',thresh)
_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)#得到轮廓信息
                                 
mask = np.zeros(imgray.shape, dtype=np.uint8)
#第三个参数使用参数 -1, 绘制填充的轮廓,,
cv2.drawContours(mask,contours,-1,255,-1)#0则绘制边界将轮廓所覆盖的地方全部画成白色
pixelpoints = np.nonzero(mask)#存储的是非0的坐标

pixelpoints1 = list(zip(pixelpoints[0],pixelpoints[1]))
pixelpoints1 =np.array(pixelpoints1)

cnt = np.reshape(pixelpoints1,(-1,1,2))
#cnt = contours
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)#计算像素最大最小值及其位置


leftmost = np.array(cnt[cnt[:,:,0].argmin()][0])
rightmost = np.array(cnt[cnt[:,:,0].argmax()][0])
topmost =np.array(cnt[cnt[:,:,1].argmin()][0])
bottommost = np.array(cnt[cnt[:,:,1].argmax()][0])

point = np.array([leftmost,rightmost,topmost,bottommost])
cv2.polylines(img,point.reshape(-1,1,2),True,(0,0,255),10 )
    
cv2.imshow('lunkuo',mask)
cv2.imshow('jizhidian',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
cv2.waitKey(0)
