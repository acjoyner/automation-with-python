import smtplib

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    with open('password.txt', 'r') as x:
        password = x.read()
    #user can give here, his email-Id of gmail.com
    server.login('anthony.c.joyner@gmail.com',password)
    subject = "Good morning from RK"
    with open('body.txt', 'r') as n:
        body = n.read()
    msg = f'subject: {subject} \n\n\n {body}'

    server.sendmail('anthony.c.joyner@gmail.com', 'anthony.c.joyner@gmail.com',msg)

    print('Message sent successfully')

if __name__ == "__main__":
    send_mail()

