import cv2
import mediapipe as mp
import pyautogui

# Initialize the video capture and hand detection modules
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Get screen dimensions
screen_width, screen_height = pyautogui.size()
    
index_x = index_y = 0

while True:
    # Read and flip the frame
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
 
            index_x = index_y = 0
            thumb_x = thumb_y = 0
            middle_x = middle_y = 0
            
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                
                if id == 8:  # first  finger 
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255), thickness=-1)
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                if id == 4:  # Thumb 
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255), thickness=-1)
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                if id == 12:  # Middle finger 
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255), thickness=-1)
                    middle_x = screen_width / frame_width * x
                    middle_y = screen_height / frame_height * y
            
            # Check for click action
            if abs(index_y - thumb_y) < 20:
                pyautogui.click()
                pyautogui.sleep(1)
            elif abs(index_y - thumb_y) < 100:
                pyautogui.moveTo(index_x, index_y)
            
            # if you  cross your hands this will  close the product
            if abs(index_x - middle_x) < 20 and abs(index_y - middle_y) < 20:
                print("Cross gesture detected. Closing the application.")
                cap.release()
                cv2.destroyAllWindows()
                break

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
