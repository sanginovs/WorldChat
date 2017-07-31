from flask import Flask
from flask.ext.mongoengine import MongoEngine

db= MongoEngine() #initializing the flask mongo engine

def create_app(**config_overrides):
    
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app) #initialize the database within the application
    
    app.config.update(config_overrides)
    '''we need to overwrite the application before we run the test'''
    '''when you run the test the new settings which are inside user/tests.py settings will be applied'''
    
    from user.views import user_app
    app.register_blueprint(user_app)
    
    from relationship.views import relationship_app
    app.register_blueprint(relationship_app)
    
    return app