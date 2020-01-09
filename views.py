from flask import render_template, request, redirect, flash,url_for,Response,send_from_directory, session
from webapp import app
import requests
from models import *
from time import strftime
import os as os
import json, sys, traceback, sendemail


captcha_secret_key = "6Le24scUAAAAACD0rA42cMoZ_EjI2lPwOImsg--b"

captcha_site_key = "6Le24scUAAAAAKDFYZo2b1qkK_DAat3PyOZmiz5U"

@app.route('/contact', methods=["POST"])
def contact():
   
    recaptcha_score = None

    url = "https://www.google.com/recaptcha/api/siteverify";

    data = {
        'secret': captcha_secret_key,
        'response': request.form['token'],
        'remoteip': request.access_route[0]
    }

    r = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
         data = data
      )

    result = r.json()

    if result['success']:
      recaptcha_score = result['score']
    else:
      recaptcha_score = 0

    if recaptcha_score > 0.5:
        try:
          sendemail.send_details_to_contact(request.form['name'],request.form['phone'],
          request.form['email'],request.form['company'],request.form['companyWebsite'],request.form['message'])
          return Response('OK')
        except:
            exceptions(sys.exc_info())
            return Response('NOT-OK')
    else:
        return Response('Captcha Failed')


@app.route('/tnc')
def tnc():
    return render_template('tnc.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Blog')
def blog():
    return redirect('/Blog/')

@app.route('/Blog/')
def blog1():
    return render_template('./Blog/index.html')

@app.errorhandler(Exception)
def exceptions(e):
    """ Logging after every Exception. """
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    app.logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return "Internal Server Error", 500
    
