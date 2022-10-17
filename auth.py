from flask import Blueprint, request, session, render_template, redirect, url_for, make_response, flash
import requests, os, json, string, random, validations as v
from db import db


auth_blueprint = Blueprint('auth_blueprint', __name__)



SUCCESS_CODE = 200
BAD_REQUEST = 400
NO_USER_CODE = 404
USER_EXISTS_CODE = 406
INTERNAL_SERVER_ERROR = 500
REDIRECT_GET = 303
REDIRECT_POST = 307
YEARS = list(range(2000,2022))


@auth_blueprint.route('/', methods=['GET'])
@auth_blueprint.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@auth_blueprint.route('/login',  methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if v.is_valid_email(email) and v.is_valid_pass(password):
       user = db.Users.find_one({'email': email},{'_id': 0})
       
       if user and password == user.get('password'):
          session["u_email"] = user.get('email')  
          
          return redirect(url_for('main_blueprint.main'))
       else:
          error_msg = 'wrong email or password'
    else:  
       error_msg = 'wrong email or password'
       
    flash(error_msg)
    return redirect(url_for('auth_blueprint.index'))


def capitalize(text):
    text = text.strip()
    text = text.split()
    out = []
    for item in text:
        cfirst = item[0].upper()
        item = cfirst+item[1:]
        out.append(item)
    return ' '.join(out)
    


@auth_blueprint.route('/logout')
def logout():
    if not session.get("u_email"):
       flash("Unauthorised to access that page, login first")
       return redirect(url_for('auth_blueprint.index'))

    session["u_email"] = None

    return redirect(url_for('auth_blueprint.index'))

