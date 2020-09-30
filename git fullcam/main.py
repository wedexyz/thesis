
import cv2
from lane import getLaneCurve
import utlis
import numpy as np
import argparse
import time
#from MotorModule import Motor

##################################################
#motor = Motor(2,3,4,17,22,27)
##################################################

#distance konfiguration
ap = argparse.ArgumentParser()
help_fd = "The ratio of focal length to sensor height (default == 905/590)"
help_dh = "Dot's height (default == 1)"
ap.add_argument("-fd", "--fdratio", required=False, help=help_fd)
ap.add_argument("-dh", "--dotheight", required=False, help=help_dh)
args = vars(ap.parse_args())
if args["fdratio"] is not None:
    fd_ratio = float(args["fdratio"])
else:
    fd_ratio = 905/590
if args["dotheight"] is not None:
    dot_height = float(args["dotheight"])
else:
    dot_height = 20



curveList = []
avgVal=10
#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://192.168.88.246:8080/video/mjpeg')
#cap = cv2.VideoCapture('video/walking.mp4')
#cap = cv2.VideoCapture('video/drive.mp4')
#cap = cv2.VideoCapture('video/vid1.mp4')
cap = cv2.VideoCapture('video/contoh.mp4')






#tensor konfiguration
thres = 0.6
classNames= []
classFile = 'model/coco.names'
configPath = 'model/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'model/frozen_inference_graph.pb'
net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')





def main():
    success, img = cap.read()
    img = cv2.resize(img,(480,240))
    curve = getLaneCurve(img,display=1)
    curve_sudut = float(curve)
    '''
    #print (curve)
    if curve < 0:
        print (" miring kiri"+" "+str(curve_sudut))

    else :
        print ('miring kanan'+" "+str(curve_sudut))
      
    
    #sen = 1.3  # SENSITIVITY
    #maxVAl= 0.3 # MAX SPEED
    if curveVal>maxVAl:curveVal = maxVAl
    if curveVal<-maxVAl: curveVal =-maxVAl
    #print(curveVal)
    if curveVal>0:
        #sen =1.7
        if curveVal<0.05: curveVal=0
    else:
        if curveVal>-0.08: curveVal=0
    #motor.move(0.20,-curveVal*sen,0.05)
    #cv2.waitKey(1)
    '''   


def tensor(): 
    success,img2 = cap.read()
    img2 = cv2.resize(img2,(500,500))
    classIds, confs, bbox = net.detect(img2,confThreshold=thres)
    cv2.line(img2,(500,250),(0,250),(0,255,0),2)
    cv2.line(img2,(250,0),(250,500),(0,255,0),2)
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img2,box,color=(0,255,0),thickness=2)
            cv2.putText(img2,classNames[classId-1].upper(),(box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,0),1)
            cv2.putText(img2,str(round(confidence*100,2))+' %',(box[0]+200,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),1)
            ## Menghitung Jarak ##
            x = box[0]
            y = box[1]
            h = box[2]
            w = box[3]
           
            #lebar = w / 20
            #yeye = y + h/3
            reye = x + (w/2) - (w/5)
            leye = x + (w/2) + (w/5)
            space = leye - reye
            f = 690
            r = 10
            distance = f * r / space
            distance_in_cm = int(distance)
            cv2.putText(img2, str(distance_in_cm)+' cm', (box[0]+100,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,255),1)
            #print(distance)
            x=box[0]
    cv2.imshow("deteksi objek",img2)
    return

def ukurantepi():
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    multiplier = fd_ratio * dot_height * height / 20
    mask = np.zeros((height, width), dtype="uint8")
    size = 600
    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 30, 150)
    (cnts, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.rectangle(image, (width//2 - size//2, height//2 - size//2),(width//2 + size//2, height//2 + size//2), (255, 0, 0), 2)

    for (i, c) in enumerate(cnts):
        ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
        if centerX >= width//2 - size//2 and centerX <= width//2 + size//2:
            if centerY >= height//2 - size//2 and \
               centerY <= height//2 + size//2:
                if radius <= size//2:
                    distance = multiplier/radius
                    print(distance)
                    #time.sleep(0.3)
                    cv2.circle(image, (int(centerX), int(centerY)),
                               int(radius), (0, 255, 0), 1)
                    cv2.putText(image, "{:.2f} cm".format(distance),
                                (int(centerX), int(centerY)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255))
    cv2.drawContours(image, cnts, 1, (0, 0, 255), 1)
    image = cv2.resize(image,(500,500))

    # Uncomment to output the recording
    # out.write(image)
    cv2.imshow("jarak tepi", image)

if __name__ == '__main__':
    
    intialTrackBarVals = [102, 80, 20, 214 ]
    utlis.initializeTrackbars(intialTrackBarVals)
    frameCounter = 0
    while True:
        main()
        tensor()
        ukurantepi()
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0
        success, img = cap.read()
        #img = cv2.resize(img,(480,240))
        #curve = getLaneCurve(img,display=1)
        #print(curve)
        #cv2.imshow('Vid',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    

