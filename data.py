# Necessary Modules

 import smtplib

# All our information goes here

 host= "smtp.gmail.com"

 port = 587

 username= "pymailmonkee@gmail.com"

 password= "reptilianoverlord"


# Setting up the connection

  email_conn = smtplib.SMTP(host,port)

  email_conn.ehlo();

# Starting up TLS, which is a secure layer for encryption

  email_conn.starttls()

# Logging into our email service

  email_conn.login(username, password)

# Sending Our Email
# This method allows us to send emails with "To Addresses" as Bcc
# Another point to be noted is that there is no Subject Line while using this method

  from_add = username
  to_add = ["thespctrl@gmail.com"]
  email_conn.sendmail(from_add,to_add,"Greetings, All Your Base are belong to Us!")

# Logging out of our email service

  email_conn.quit()


# Another method is by using an instance of the SMTP Class

  from smtplib import SMTP

# Setting up the connection

  email_conn2 = SMTP(host, port)
  email_conn2.ehlo();

# Starting up TLS, which is a secure layer for encryption

  email_conn2.starttls()

# Logging into our email service

  email_conn2.login(username, password)

# Sending Our Email

  from_add = username
  to_add = ["thespctrl@gmail.com"]
  email_conn2.sendmail(from_add,to_add,"Greetings, All Your Base are belong to Us!")
  
# Logging out of our email service

  email_conn2.quit()

# Handling Exceptions in Code

  from smtplib import SMTP, SMTPAuthenticationError, SMTPException

# Setting up the connection

  email_conn3 = SMTP(host, port)
  email_conn3.ehlo();

# Starting up TLS, which is a secure layer for encryption

  email_conn3.starttls()

# Logging into our email service
 try:
     email_conn3.login(username, "incorrect_password")
     email_conn3.sendmail(from_add,to_add,"Greetings, All Your Base are belong to Us!")

 except SMTPAuthenticationError:
     print("Could Not Login")

 except:
     print("Oops... An Error Ocurred")

 # Logging out of our email service

   email_conn3.quit()
