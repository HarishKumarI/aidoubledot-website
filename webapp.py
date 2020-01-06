from flask import Flask
import os as os
import sendgrid
import logging
from envparse import env
import sys
from datetime import date

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/tsoai'
#app.config['SQLALCHEMY_DATABASE_URI'] = env.str('DATABASE_URL')
app.config['GAGTM_CODE'] = env.str('GAGTM_CODE')
#app.config['RAZOR_ID'] = env.str('RAZOR_ID')
#app.config['RAZOR_SECRET'] = env.str('RAZOR_SECRET')
#app.config['PAISE_CONVERSION'] = env.float('PAISE_CONVERSION',default=100)
app.config['DEBUG'] = env.bool('DEBUG', default=False)
#app.config['FORCE_SSL'] = env.bool('FORCE_SSL', default=False)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

sg = sendgrid.SendGridAPIClient(api_key=env.str('SENDGRID_API_KEY'))
#razorpay_client = razorpay.Client(auth=(env.str('RAZOR_ID'), env.str('RAZOR_SECRET')))

from views import *

if 'DYNO' in os.environ:
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.INFO)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

    # app.run()


