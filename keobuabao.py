import cv2
import mediapipe as mp # type: ignore

class handDetector():
    def __init__(self) :
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands()
        self.mpDraw=mp.solutions.drawing_utils

    def findHand(self,img):
        #change BGR from cv2 to RGB from meidapipe
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        #Give image to mediapipe library
        result=self.hands.process(imgRGB)
        handlms=[]
        #Check and draw hand
        if result.multi_hand_landmarks:
            for handlm in result.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img,handlm,self.mpHands.HAND_CONNECTIONS)
            
            #Show the coordinates of fingers
            firstHand=result.multi_hand_landmarks[0]
            h,w,_=img.shape
            for id,lm in enumerate(firstHand.landmark):
                real_x,real_y=int(lm.x *w),int(lm.y*h)
                handlms.append([id,real_x,real_y])
        return img,handlms
    
    #Return the quantity of fingers from the list
    def count_finger(self,hand_lm):
        finger_start_index=[4,8,12,16,20]
        n_finger=0
        
        if len(hand_lm)>0:
            #check thumb
            if hand_lm[finger_start_index[0]][1]< hand_lm[finger_start_index[0]-1][1]:
                n_finger+=1
            #check the last 4 fingers:
            for id in range(1,5):
                if hand_lm[finger_start_index[id]][2]< hand_lm[finger_start_index[id]-2][2]:
                     n_finger+=1
                
        else:
            return -1
        return n_finger
