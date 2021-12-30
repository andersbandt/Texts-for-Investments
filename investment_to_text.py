# Texts-for-Investments
Sends a phone number investment data

from googlefinance import getQuotes
import json
import smtplib
from email.mime.text import MIMEText


info = getQuotes("Your stock ticker") # For example: "AAPL", "MSFT", etc.

stuff = json.dumps(info)

final = ""

for i in range(118,123):
	 final += stuff[i]

price = float(final)

value = price * 128.514
totalnet = value - 3200

if totalnet < -300:
	message = "Hmm.. things are looking rough. Your net loss is %s" % totalnet

if totalnet < 0:
	"At least you aren't dead! Your total net loss is %s" % totalnet

if totalnet > 0 and totalnet < 50:
	"At least you're above 0! Your total net gain is %s" % totalnet

if totalnet > 300:
	"Wow you're doing amazing! Your total net gain is %s" % totalnet

print message

me = "your email here"
to = "your phone number"@vtext.com"
login = "your gmail address"
password = "your password"
smptserver = "smtp.gmail.com:587"


def sendemail(sender, to, message, login,
	password, smptserver):

	server = smtplib.SMTP(smptserver)
	server.starttls()
	server.login(login,password)
	problems = server.sendmail(sender, to, message)

sendemail(me, to, message, login, password, smptserver)


