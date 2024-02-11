
import cv2
import os




camera = cv2.VideoCapture(0)

def gen_frames():
   
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
           
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            
            


def save_image():
    
    
    
 frame_count = 0
    
    


# Define the directory to save the images
 SAVE_DIR = 'saved_frames'

# Create the directory if it does not exist
 os.makedirs(SAVE_DIR, exist_ok=True)

 success, frame = camera.read()
    
       
  # Save the frame as an image
 filename = os.path.join(SAVE_DIR, f'frame_{frame_count}.jpg')
 cv2.imwrite(filename, frame)

 
 DIR = f"{SAVE_DIR}/frame_{frame_count}.jpg"
 
 return DIR
 
 
            

           
   
 
