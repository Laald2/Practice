#pylint=disable
import smtplib
import requests,time

def check():
    '''
    recursivly call check until system is online    
    '''
    try:
        requests.get('https://www.google.com').status_code
        print('online')
        time.sleep(5)
    except:
        print('offline')
        time.sleep(5)
        check()
check()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("RaspberryPoEEGR390@gmail.com","Harvey390")
MSG = "hello"
server.sendmail("4106279601@tmomail.net", MSG)
server.quit()
