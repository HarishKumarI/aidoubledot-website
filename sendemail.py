from webapp import sg,app
import json
import os as os
from sendgrid.helpers.mail import *


def send_confirmation_email(user, order, payment_info, url_root):
    from_email = Email("info@theschoolofai.com", "Info @ TSOAI")
    to_email = Email(user['email'], user['name'])
    reply_email = Email(os.environ['CONTACT_EMAIL'])
    subject = "Registration confirmed"

    file_path = './templates/email_confirm_saturday.html'

    if order['batch'] == 'batch2':
        file_path = './templates/email_confirm_sunday.html'

    email_file = open(file_path, 'r')
    text = email_file.read().strip()
    email_file.close()

    html_body = text.format(name=user['name'], order_id=order['orderId'], payment_id=payment_info['id'], amount=payment_info['amount'], url_root=url_root)

    content = Content("text/html", html_body)

    email = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=email.get())
    return "OK"


def send_details_to_contact(name, phone, customerEmail, company, companyWebsite, message):
    from_email = From("info@aidoubledot.com", "AI Double Dot")
    to_email = To(os.environ['CONTACT_EMAIL'])
    reply_email = Email(os.environ['CONTACT_EMAIL'])
    subject = "Corporate Contact"

    body = "<html><body><table><tr><td> Name: </td><td>"+name+"</td></tr> <tr><td> Phone: </td><td>"+phone +\
           "</td></tr> <tr><td> Email: </td><td>"+customerEmail+"</td></tr> <tr><td> Company: </td><td>"+company +\
           "</td></tr> <tr><td>  Company Website: </td><td>"+companyWebsite+"</td></tr> <tr><td> Message: </td><td>" +\
           message+"</td></tr></table></body></html>"
    content = Content("text/html", body)

    mail = Mail(from_email=from_email, to_emails=to_email, subject=subject, html_content=body)
    # response = sg.client.mail.send.post(request_body=mail.get())
    response = sg.send(mail)
    return "OK"
