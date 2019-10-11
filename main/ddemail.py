import smtplib
def em(address,task):
	fromaddr = 'singhdhruv498@gmail.com'
	toaddrs  = str(address)
	msg = "RICHIE IS GOING FOR "+str(task)
	username = 'singhdhruv498@gmail.com'
	password = 'iamdhrmsha'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
