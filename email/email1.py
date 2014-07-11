#!/usr/bin/python

import smtplib
import socket
from email.mime.text import MIMEText

email_server = "somesmtp@google.com"
email_from = "rd-cloud-tools@google.com"
email_to = "je@google.com"

def main():
    send_email("email content")


def send_email(content):
    msg = MIMEText(content)
    msg["Subject"] = "email from {0}".format(socket.getfqdn())
    msg["From"] = email_from
    msg["To"] = email_to

    smtp = smtplib.SMTP(email_server)
    smtp.sendmail(msg["From"], [msg["To"]], msg.as_string())
    smtp.quit()


main()