import face_recognition
import cv2
from scipy.spatial import distance as dist
import playsound
from threading import Thread
import numpy as np



MIN_AER = 0.30
EYE_AR_CONSEC_FRAMES = 10
YAWN_THRESH=25

COUNTER = 0
ALARM_ON = False
AlARM=False

def eye_aspect_ratio(eye):
 # compute the euclidean distances between the two sets of
 # vertical eye landmarks (x, y)-coordinates
 A = dist.euclidean(eye[1], eye[5])
 B = dist.euclidean(eye[2], eye[4])

 # compute the euclidean distance between the horizontal
 # eye landmark (x, y)-coordinates
 C = dist.euclidean(eye[0], eye[3])

 # compute the eye aspect ratio
 ear = (A + B) / (2.0 * C)

 # return the eye aspect ratio
 return ear


def lip_distance(top,bottom):
    top_lip = top[1:5]
    top_lip = np.concatenate((top_lip, top[7:11]))

    low_lip = bottom[1:5]
    low_lip = np.concatenate((low_lip, bottom[7:11]))

    top_mean = np.mean(top_lip, axis=0)
    low_mean = np.mean(low_lip, axis=0)

    distance = abs(top_mean[1] - low_mean[1])
    return distance







def sound_alarm(alarm_file):
 # play an alarm sound
 playsound.playsound(alarm_file)

    
def alarm(alarm_file):
 # play an alarm sound
 playsound.playsound(alarm_file)
 
def main():
    global COUNTER
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read(0)

        # get it into the correct format
        #small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # get the correct face landmarks
        
        face_landmarks_list = face_recognition.face_landmarks(frame)

            # get eyes
        for face_landmark in face_landmarks_list:
                        leftEye = face_landmark['left_eye']
                        rightEye = face_landmark['right_eye']
                        topLip=face_landmark['top_lip']
                        bottomLip=face_landmark['bottom_lip']
        
                        #eye aspect ratio for left and right eyes
                        leftEAR = eye_aspect_ratio(leftEye)
                        rightEAR = eye_aspect_ratio(rightEye)
                        # average the eye aspect ratio together for both eyes
                        ear = (leftEAR + rightEAR) / 2
                        #========================converting left and right eye values in numpy arrays
                        lpts = np.array(leftEye)
                        rpts = np.array(rightEye)
                        #==================showing line from left of left eye and right of right eye
                        cv2.polylines(frame, [lpts],True ,(255,255,0), 1)
                        cv2.polylines(frame, [rpts],True ,(255,255,0), 1)
                        
                        lpoints = np.array(topLip)
                        rpoints = np.array(bottomLip)
                        #==================showing line from left of left eye and right of right eye
                        cv2.polylines(frame, [lpoints],True ,(255,255,0), 1)
                        cv2.polylines(frame, [rpoints],True ,(255,255,0), 1)
                        
                        # check to see if the eye aspect ratio is below the blink
                        # threshold, and if so, increment the blink frame counter
                        if ear < MIN_AER:
                                COUNTER+= 1

                                # if the eyes were closed for a sufficient number of times
                                # then sound the alarm
                                if COUNTER >= EYE_AR_CONSEC_FRAMES:
                                        # if the alarm is not on, turn it on
                                        if not ALARM_ON:
                                                ALARM_ON = True
                                                t = Thread(target=sound_alarm,
                                                                args=('alarm.wav',))
                                                t.deamon = True
                                                t.start()

                                        # draw an alarm on the frame
                                        cv2.putText(frame, "ALERT! You are feeling asleep!", (10, 30),
                                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        # otherwise, the eye aspect ratio is not below the blink
                        # threshold, so reset the counter and alarm
                        else:
                                COUNTER = 0
                                ALARM_ON = False
                                
                        
                        dis=lip_distance(topLip,bottomLip)
                        if (dis > YAWN_THRESH):
                                cv2.putText(frame, "Yawn Alert", (10, 30),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                                if not ALARM:
                                    ALARM = True
                                    x = Thread(target=alarm, args=('alarm1.wav',))
                                    x.deamon = True
                                    x.start()
                        else:
                            ALARM = False

                        cv2.putText(frame, "EAR: {:.2f}".format(ear), (500, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        
                        cv2.putText(frame, "YAWN: {:.2f}".format(dis), (300, 60),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        # show the frame
                        cv2.imshow("Sleep detection program.", frame)

        # if the `q` key was pressed, break from the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    video_capture.release()
    cv2.destroyAllWindows()

main()