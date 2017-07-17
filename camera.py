import numpy as np
import cv2
# from pyvision.types.img import Image
import pyvision as pv
import ocof.filters.common as common
import ocof
import time

cap = cv2.VideoCapture(0)

global src
global flagDraw 
flagDraw = False

def onMouseEvent(event,x,y,flags,param):  
    global startPointx   
    global startPointy   
    global flagDraw    
    global src
    # print event
    if(event==1):  
        print "Position is: %d,%d" ,x,y   
        startPointx = x  
        startPointy = y  
        flagDraw = True  
    if(event==0):  
        if(flagDraw==True):  
            # image = cv.CloneImage(src) 
            image = src.copy()
            cv2.rectangle(image, (startPointx,startPointy), (x,y), (255,0,0),3)  
            cv2.imshow("capture", image)  
             
            print "EndPosition is: %d,%d" ,x,y    
    if(event==4):  
        if(flagDraw==True):  
            # image = cv.CloneImage(src)
            image = src.copy()
            cv2.rectangle(image, (startPointx,startPointy), (x,y), (255,0,0),3)  
            cv2.imshow("capture", image) 
            flagDraw = False
            global TAZ_RECT
            TAZ_RECT = pv.Rect(startPointx,startPointy,x-startPointx,y-startPointy)


if __name__ == '__main__':
	# while(1):
	#     # get a frame
	#     ret, frame = cap.read()
	#     # show a frame
	#     cv2.imshow("capture", frame)
	#     if cv2.waitKey(1) & 0xFF == ord('q'):
	#         break
	# cap.release()
	# cv2.destroyAllWindows() 
	global src
	tracker = None

	ret, frame = cap.read()
	    # show a frame
	print "originImg message:"
	print frame.shape
	print frame.dtype
	print isinstance(frame,np.ndarray)

	src = frame.copy()

	GrayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	print "grayImg message:"
	print GrayImg.shape
	print GrayImg.dtype
	print isinstance(GrayImg,np.ndarray)

	bufferimg = GrayImg.transpose().tostring()
	print "bufferImg message:"
	# print bufferimg.shape
	# print bufferimg.dtype
	print isinstance(bufferimg,np.ndarray)
	print isinstance(bufferimg,str)

	cv2.imshow("capture", frame)
	cv2.setMouseCallback("capture", onMouseEvent)
	cv2.waitKey()
	# cap.release()
	cv2.destroyAllWindows()
	# TAZ_RECT = pv.Rect(200,60,120,120)
	# print TAZ_RECT
	
	i = 0

	# Frame = pv.Image(frame)
	# tracker = ocof.MOSSETrack(Frame,TAZ_RECT)
	# tracker.update(Frame)

	print "im here!!!"
	while(1):
		ret, frame = cap.read()
		# print frame.shape
		Frame = pv.Image(frame)
		print "Processing Frame %d..."%i
		if tracker == None:
			tracker = ocof.MOSSETrack(Frame,TAZ_RECT)
			print "init"
		else:
			start = time.time()
			tracker.update(Frame)
			stop = time.time()
			print "period:",(stop-start)
			i += 1
			rect = tracker.rect
			show = (Frame.asOpenCV()).copy()
			cv2.rectangle(show, ((int)(rect.x),(int)(rect.y)), ((int)(rect.x+rect.w),(int)(rect.y+rect.h)), (255,0,0),2)
			cv2.imshow("show", show)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()
    	