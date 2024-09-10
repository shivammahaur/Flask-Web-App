from flask import Flask

def create_app():
    '''
    Creates and returns a flask app
    '''
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    return app