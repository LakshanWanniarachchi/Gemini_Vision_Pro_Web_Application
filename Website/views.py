from flask import Blueprint , render_template ,Response , request ,jsonify
from .video import gen_frames , save_image
from .GeminiVisionpro_genarater import genarate_text
import json
import base64
import os




views = Blueprint('views' ,__name__)


@views.route('/')
def Ai():
    
   return render_template("Gemini_Vition_Pro.html")




@views.route('/bla')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
 
 
 
 
@views.route('/get_image', methods=['POST'])
def get_image():
   
   
   
   if request.method == 'POST':
      
      text = request.json
      
      image_url =text.get('image_data')
      message = text.get('message')
      
      
      
     
      
     # Decode Base64 image data
      _, encoded_data = image_url.split(",", 1)
      decoded_data = base64.b64decode(encoded_data)

    # Save the decoded image data to a file
      with open('saved_frames/uploaded_image.png', 'wb') as f:
        f.write(decoded_data)

     
     
      image_path= "saved_frames/uploaded_image.png"
   
      
   
      comments = genarate_text(image_path,message )
      
      print(comments)
   
      return jsonify(comments)
      
      

   
   
   
   
   
   
   
    
    

