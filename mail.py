import smtplib
def maildude(name,address,msg2):
    fromaddr="TheWebsiteWizard01@gmail.com"
    toaddr="victorgaitour@gmail.com"
    msg=name+"\n"+address+"\n"+msg2
    print msg
    username = 'TheWebsiteWizard01@gmail.com'
    password = ''
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    try:
        server.login(username,password)
        server.sendmail(fromaddr, toaddr, msg)
    except:
        server.quit()
        return False
    server.quit()
    return True

