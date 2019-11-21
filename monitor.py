import os 
import requests
import smtplib

EMAIL_ADRESS = os.environ.get('EMAIL_BRAN')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

r = requests.get('http://google.com', timeout=5)#set timeout for 5ms, to stop constant waiting

# check if status code is 200, 
if r.status_code != 200: 
	with smtplib.SMTP('smtp.gmail.com', 587) as smtp
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		#start a encrypted connection with gamil through smtp

		smtp.login(EMAIL_ADRESS,EMAIL_PASS)
		#getting the email adress and passware from envirnmental variables

		subject = 'Google IS DOWN'
		body = 'Google IS DOWN'
		msg = f'Subject: {subject}/n/n{body}'

		smtp.sendmail(EMAIL_ADRESS,EMAIL_ADRESS, msg)#sender, reciever and message

		
