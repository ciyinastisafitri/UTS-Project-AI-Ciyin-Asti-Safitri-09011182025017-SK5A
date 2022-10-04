#Importing modules
import numpy as np
import cv2
#Webcam video capture
cap = cv2.VideoCapture(0)

while(1):
    #Reading the video 
    #Webcam in image frames
    _, img = cap.read()
    
    #Converting frame(img == BGR) to HSV(hue-saturation-value)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #Define range of red color in HSV
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    
    #Define range of blue color in HSV
    blue_lower = np.array([99, 115, 150], np.uint8)
    blue_upper = np.array([110, 255, 255], np.uint8)
    
    #Define range of yellow color in HSV
    yellow_lower = np.array([22, 60, 200], np.uint8)
    yellow_upper = np.array([60, 255, 255], np.uint8)
    
    #Define range of green color in HSV
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    
    #Finding the range  of red,blue,yellow,green colors in the image
    #Define mask
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    green = cv2.inRange(hsv, green_lower, green_upper)
    
    #Morphological transformation, Dilation 
    kernal = np.ones((5,5), "uint8")
    
    red = cv2.dilate(red, kernal)
    res = cv2.bitwise_and(img, img, mask=red)
    
    blue = cv2.dilate(blue, kernal)
    res1 = cv2.bitwise_and(img, img, mask=blue)
    
    yellow = cv2.dilate(yellow, kernal)
    res2 = cv2.bitwise_and(img, img, mask=yellow)
    
    green = cv2.dilate(green, kernal)
    res3 = cv2.bitwise_and(img, img, mask=green)
    
    #Creating contour to track red color
    (contours, hierarchy) = cv2.findContours(
        red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(img, "Merah", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
    
    #Creating contour to track blue color      
    (contours, hierarchy) = cv2.findContours(
        blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, "Biru", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
    
    #Creating contour to track yellow color       
    (contours, hierarchy) = cv2.findContours(
        yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.putText(img, "Kuning", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255))
    
    #Creating contour to track green color       
    (contours, hierarchy) = cv2.findContours(
        green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "Hijau", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
    
    #Program Termination       
    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break