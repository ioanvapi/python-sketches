#!/usr/bin/python

import commands
import datetime
import smtplib
import socket

from email.mime.text import MIMEText

limit_percent = 20
email_to = "je@google.com"


def main():
    output = commands.getoutput("free -m")
    output_array = output.split()
    total = int(output_array[7])
    free = int(output_array[9])
    buffers = int(output_array[11])
    cached = int(output_array[12])
    actual_free = free + buffers + cached

    percent_free = actual_free * 100 / total
    print("Percent free: {0}%".format(percent_free))

    if percent_free < limit_percent:
        ps_aux = commands.getoutput("ps aux")
        with open("./ps_aux.out", "a") as f:
            f.write("\n\n##################################\n")
            ps_aux = "Current time: {0}\n".format(datetime.datetime.now()) + ps_aux
            f.write(ps_aux)
            send_email(ps_aux)


def send_email(content):
    msg = MIMEText(content)
    msg["Subject"] = "Alert PS_AUX from {0}".format(socket.getfqdn())
    msg["From"] = "rd-cloud-tools@server.com"
    msg["To"] = email_to

    smtp = smtplib.SMTP("some.smtp.net")
    smtp.sendmail(msg["From"], [msg["To"]], msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    main()