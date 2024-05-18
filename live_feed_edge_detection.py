import cv2
from pathlib import Path

def canny_edge_detection(frame): 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5) 
    edges = cv2.Canny(blurred, 70, 135) 
    return blurred, edges

def main(): 
    # Open the default webcam  
    cap = cv2.VideoCapture(2) 
      
    while True: 
            ret, frame = cap.read() 
            if not ret: 
                print('Image not captured') 
                break
              
            # Perform Canny edge detection on the frame 
            blurred, edges = canny_edge_detection(frame) 
              
            # Display the original frame and the edge-detected frame 
            #cv2.imshow("Original", frame) 
            cv2.imshow("Blurred", blurred) 
            cv2.imshow("Edges", edges) 
              
            # Exit the loop when 'q' key is pressed 
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
          
        # Release the webcam and close the windows 
    cap.release() 
    cv2.destroyAllWindows()

if __name__ == "__main__": 
    main()
