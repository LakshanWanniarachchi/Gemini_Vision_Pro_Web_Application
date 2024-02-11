from flask import Flask



def create_app():
    
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gemini_ai_web_project'
    
    
    from .views import views
    
    
    app.register_blueprint(views , url_prefix="/")
    
    
    return app