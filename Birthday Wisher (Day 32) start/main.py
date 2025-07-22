import smtplib

my_email = 'naofumii919@gmail.com'
password = '5378231'
rec_mail = 'eholmes294@gmail.com'
connection = smtplib.SMTP('smptp.gmail.com')

# Make the message encrypted, secure connection
connection.starttls()

connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=rec_mail, msg='Hello')
connection.close()