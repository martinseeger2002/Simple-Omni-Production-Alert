# Importing libraries
import time
from playsound import playsound

import hashlib
from urllib.request import urlopen, Request
from datetime import datetime
# setting the URL you want to monitor
url = Request('https://explorer.omnilite.org/ltc/properties/production',
			headers={'User-Agent': 'Mozilla/5.0'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("Checking OmniLite Explorer")

time.sleep(10)

while True:
	try:
		# perform the get request and store it in a var
		response = urlopen(url).read()
		
		# create a hash
		currentHash = hashlib.sha224(response).hexdigest()
		
		# wait for 150 seconds
		time.sleep(150)
		
		# perform the get request
		response = urlopen(url).read()
		
		# create a new hash
		newHash = hashlib.sha224(response).hexdigest()
		# get date current time
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		# check if new hash is same as the previous hash
		if newHash == currentHash:		
			continue

		# if something changed in the hashes
		else:
			# notify
			playsound("newproperty.mp3")
			print("New property detected.")
			print("Current Time =", current_time)
			# again read the website
			response = urlopen(url).read()

			# create a hash
			currentHash = hashlib.sha224(response).hexdigest()

			# wait for 30 seconds
			time.sleep(30)
			continue
			
	# To handle exceptions
	except Exception as e:
		print("error")

