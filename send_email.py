#!/usr/bin/env python3
"""===============================================================================

        FILE: ./test2.py

       USAGE: (not intended to be directly executed)

 DESCRIPTION: 

     OPTIONS: ---
REQUIREMENTS: ---
        BUGS: ---
       NOTES: ---
      AUTHOR: Alex Leontiev (alozz1991@gmail.com)
ORGANIZATION: 
     VERSION: ---
     CREATED: 2021-08-05T09:21:42.906637
    REVISION: ---

==============================================================================="""
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import os
import click
import tqdm
import time
import itertools

@click.command()
@click.option("-r","--recipient",default=os.environ["CANDICE_EMAIL"])
def send_email(recipient):
#    os.system(f"rm -rf screenshots/*.png")
#    for i in range(4):
#        os.system("node index.js {i}")
#        time.sleep(2)

    gmail_user = os.environ["GOOGLE_ACCOUNT"]
    gmail_password = os.environ["GOOGLE_PASS"]
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    _send_mail(gmail_user, list({recipient, gmail_user}), "test subject", "test test", files=[
              f"screenshots/page_{k}_{i}.png" for k,i in itertools.product(["bottom"],range(4))], server=server)
    server.close()
    click.echo(f"sent email to {recipient}")



def _send_mail(send_from, send_to, subject, text, files=None,
              server=None):
    """
    adapted from https://stackoverflow.com/a/3363254
    """
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)


#    smtp = smtplib.SMTP(server)
    if server is None:
        server = smtplib.SMTP("127.0.0.1")
    smtp = server
    smtp.sendmail(send_from, send_to, msg.as_string())
#    smtp.close()


if __name__=="__main__":
    send_email()
