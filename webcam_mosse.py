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
        startPointx = x  
        startPointy = y  
        flagDraw = True  

    if(event==0):  
        if(flagDraw==True):  
            # image = cv.CloneImage(src) 
            image = src.copy()
            cv2.rectangle(image, (startPointx,startPointy), (x,y), (255,0,0),3)  
            cv2.imshow("capture", image) 

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
	global src
	tracker = None

	ret, frame = cap.read()

	src = frame.copy()

	cv2.imshow("capture", frame)
	cv2.setMouseCallback("capture", onMouseEvent)
	cv2.waitKey()
	cv2.destroyAllWindows()
	
	i = 0
	while(1):
		ret, frame = cap.read()
		# print frame.shape
		Frame = pv.Image(frame)
		print "Processing Frame %d..."%i
		i += 1
		if tracker == None:
			tracker = ocof.MOSSETrack(Frame,TAZ_RECT)
		else:
			start = time.time()
			tracker.update(Frame)
			stop = time.time()
			print ('update in %.4f s' % (stop-start))
			rect = tracker.rect
			show = (Frame.asOpenCV()).copy()
			cv2.rectangle(show, ((int)(rect.x),(int)(rect.y)), ((int)(rect.x+rect.w),(int)(rect.y+rect.h)), (255,0,0),2)
			cv2.imshow("show", show)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
	cap.release()
	cv2.destroyAllWindows()
    	