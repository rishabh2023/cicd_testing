import smtplib
SenderAddress = "bestlib01@gmail.com" 
# Here Enter Senders Email address
passwrd1  = 'buyxjsuqainevdpl'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(SenderAddress,passwrd1)
msg = 'Hello Dear,Congratulations Your CICD model run successfully from \n Our Best wishes with you. \n Email1\nThankyou' 
subject = 'Congratulations Your account Successfully Activated'
body = 'subject:{}\n\n{}'.format(subject,msg)
server.sendmail(SenderAddress,'sahuji2607@gmail.com',body)
server.quit() 
print('Email sent...')