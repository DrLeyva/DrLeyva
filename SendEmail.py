import smtplib
import ssl


def SendEmail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "noreply.leyva@gmail.com"
    password = "hvun danr yajn wfvg"
    receiver = "noreply.leyva@gmail.com"
    context = ssl.create_default_context()


    #message = """\
    #Subject:Thank you for reaching Dr.Leyva
   # Thank you for reaching Dr. Leyva.\n\nThis email is an example of how I automated a contact page using Python.
    #"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
