import random
import cv2
import keobuabao as handlib
import os



detector=handlib.handDetector()

camera=cv2.VideoCapture(0)

def draw_results(frame,user_draw):
    #computer random
    com_draw=random.randint(0,2)

    
     # Vẽ hình, viết chữ theo user_draw
    frame = cv2.putText(frame, 'You', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2, cv2.LINE_AA)

    s_img = cv2.imread(os.path.join("F:/python/cv/image", str(user_draw) + ".png"))
    
    x_offset = 50
    y_offset = 100
    frame[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img

    # Vẽ hình, viết chữ theo com_draw
    frame = cv2.putText(frame, 'Computer', (400, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)
    s_img = cv2.imread(os.path.join("F:/python/cv/image",str(com_draw) + ".png"))
    x_offset = 400
    y_offset = 100
    frame[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img

    if user_draw == com_draw:
        result="DRAW!"
    elif (user_draw==0) and (com_draw==1):
        result="YOU WIN!"
    elif (user_draw==1) and (com_draw==2):
        result="YOU WIN!"
    elif (user_draw==2) and (com_draw==0):
        result="YOU WIN!"
    else:
        result="YOU LOSE!"

    frame = cv2.putText(frame, result, (300, 450), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 0, 255), 2, cv2.LINE_AA)



while True:
    ret, frame=camera.read()
    frame=cv2.flip(frame,1)

    #Send image to detector
    frame, hand_lm =detector.findHand(frame)
    n_finger=detector.count_finger(hand_lm)
    user_draw=-1
    if n_finger==0:
        user_draw=1
    elif n_finger ==2:
        user_draw=2
    elif n_finger ==5:
        user_draw=0
    elif n_finger!=-1:
        print('Rock Paper Scissor,PLS')
    else:
        print('HAND IS NOT DETECTED')
    cv2.imshow('game',frame)
    if cv2.waitKey(1)==ord('q'):
        break
    elif cv2.waitKey(1)==ord(' '):
        draw_results(frame,user_draw)
        cv2.imshow('game',frame)
        cv2.waitKey()
camera.release()
cv2.destroyAllWindows()