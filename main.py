from flask import Blueprint, request, session, render_template, redirect, url_for, jsonify, make_response, flash
import requests, os, json, time, codecs, csv, validations as v
from db import db
from bson import ObjectId, json_util #for serializing mongodb objects.


main_blueprint = Blueprint('main_blueprint', __name__)


SUCCESS_CODE = 200
BAD_REQUEST = 400
NO_USER_CODE = 404
USER_EXISTS_CODE = 406
INTERNAL_SERVER_ERROR = 500
REDIRECT_GET = 303
REDIRECT_POST = 307

           
@main_blueprint.route('/main', methods=['GET'])
def main():
    if not session.get("u_email"):
       flash("Unauthorised access, login first")
       return redirect(url_for('auth_blueprint.index'))

    user = {'email': session.get("u_email")}
    return render_template('main.html', user=user)


@main_blueprint.route('/main/get_questions',  methods=['GET'])
def get_questions():
    email = session.get("u_email")
    if not email:
       flash("Unauthorised access, login first")
       return redirect(url_for('auth_blueprint.index'))
       
    user = db.Users.find_one({'email': email})

    questions = db.Questions.find({"$or":[{"email1":email},{"email2":email}]}).limit(100)
    questions = list(questions)
    if email == questions[0].get('email1'): 
       for q in questions:
           q['answer'] = q.get('answer1')
    elif email == questions[0].get('email2'): 
       for q in questions:
           q['answer'] = q.get('answer2')
    
   
        
    questions  = json_util.dumps(questions)
    response =  make_response(questions, SUCCESS_CODE) 
     
    return (response)


@main_blueprint.route('/main/save_answers',  methods=['POST'])
def save_answers():
    email = session.get("u_email")
    if not  email:
       flash("Unauthorised access, login first")
       return redirect(url_for('auth_blueprint.index'))
      
    questions = request.get_json()

    if email == questions[0].get('email1'):
       for q in questions:   
           db.Questions.update_one({'number': q.get('number')},{"$set": { 'answer1' : q.get('answer')}})
    elif email == questions[0].get('email2'):
       for q in questions:   
           db.Questions.update_one({'number': q.get('number')},{"$set": { 'answer2' : q.get('answer')}})  
    
      
          
    response =  make_response("answer saved successfully", SUCCESS_CODE) 
     
    return (response)




 

 

