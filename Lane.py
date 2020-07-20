import cv2
import numpy as np
import matplotlib.pyplot as plt
webcam=False
cap=cv2.VideoCapture('video.mp4')

def roi(image):
	height=image.shape[0]
	triangle=np.array([[(150,height),(325,265),(435,450)]])
	mask=np.zeros_like(image)
	cv2.fillPoly(mask,triangle,255)
	crop=cv2.bitwise_and(image,mask)
	return crop

def display_line(image,lines):
	line_image=np.zeros_like(image)
	if lines is not None:
		for line in lines:
			x1,y1,x2,y2=line.reshape(4)
			cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),10)
	return line_image
while True:
	if webcam:
		sucesss,img=cap.read()
	else:
		img=cv2.imread('shimla.jpg')
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur=cv2.GaussianBlur(gray,(5,5),0)
	canny=cv2.Canny(blur,50,150)
	region=roi(canny)
	lines=cv2.HoughLinesP(region,2,np.pi/180,100,np.array([]),minLineLength=30,maxLineGap=5)
	line_image=display_line(img,lines)
	combined=cv2.addWeighted(img,0.8,line_image,1,1)
	cv2.imshow('Lane',combined)
	if cv2.waitKey(1) &  0XFF==ord('q'):
		break


	