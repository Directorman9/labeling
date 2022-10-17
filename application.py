from flask import Flask, session, request, render_template, jsonify, url_for, make_response
from flask_session import Session
from auth import auth_blueprint
from main import main_blueprint
import os, requests 


application = Flask(__name__)

application.config['SECRET_KEY'] = "labelling_secret"
application.config["SESSION_TYPE"] =  "filesystem"
application.config["SESSION_FILE_DIR"] = "sessnz"
application.config["SESSION_PERMANENT"] = False #destroy session when browser closes

application.register_blueprint(auth_blueprint)
application.register_blueprint(main_blueprint)

Session(application)

if __name__ == "__main__":
   #application.run(host='0.0.0.0', debug=True, port=6543)
   application.run(host='0.0.0.0', debug=True)
   #application.run(host='0.0.0.0')







