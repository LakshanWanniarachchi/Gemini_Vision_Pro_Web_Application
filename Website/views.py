from flask import Blueprint , render_template ,Response , request ,jsonify
from .video import gen_frames , save_image
from .GeminiVisionpro_genarater import genarate_text
import json

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
      
      print("json data"+text)
   
      DIR = save_image()
   
      text = genarate_text(DIR,text )
      
      print(text)
   
      
      
      

      return jsonify(text)  
   
   
   
   
   
   
   
    
    

