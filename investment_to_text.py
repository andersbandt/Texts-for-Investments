# Texts-for-Investments
# PROGRAM DESCRIPTION: Sends a phone number investment data
# 	A good use case might be running this on a server once a day to get stock updates.

from googlefinance import getQuotes
import json
import smtplib
from email.mime.text import MIMEText

# user needed information to run program
ticker = "Your stock ticker"
buy_price = 0 # price for purchasing the stock

me = "your email here"
to = "your phone number"
to = to + "@vtext.com" # NOTE: I think this only works for Verizon phone numbers
login = "your gmail address"
password = "your password"
smptserver = "smtp.gmail.com:587" # most likely don't need to change


# get stock information
info = getQuotes(ticker) # For example: "AAPL", "MSFT", etc.
stuff = json.dumps(info)
final = ""
for i in range(118,123):
	 final += stuff[i]
price = float(final)

value = price * 128.514
totalnet = value - buy_price


# set up some ranges (in dollars) to change your message
net_low_range = -300
net_high_range = 300


# conditionals to form message based on net gain
if totalnet < net_low_range:
	message = "Hmm.. things are looking rough. Your net loss is %s" % totalnet
elif totalnet < 0:
	message = "At least you aren't dead! Your total net loss is %s" % totalnet
elif totalnet > 0 and totalnet < net_high_range:
	message = "At least you're above 0! Your total net gain is %s" % totalnet
elif totalnet > net_high_range:
	message = "Wow you're doing amazing! Your total net gain is %s" % totalnet

print(message)

# create send email funcion
def sendemail(sender, to, message, login, password, smptserver):
	server = smtplib.SMTP(smptserver)
	server.starttls()
	server.login(login,password)
	problems = server.sendmail(sender, to, message)

# send the email
sendemail(me, to, message, login, password, smptserver)


