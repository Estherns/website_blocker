import time
from datetime import datetime as dt 

host_file = 'hosts' 
#Normally the host file is located on the path below, therefore when it comes to actual project implementation, change host_file to host_path
#host_path = r'C:\Windows\System32\drivers\etc\hosts

# initialize the redirect path
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'twitter.com']

while True:
	# condition to check if current time is within the working hours and append the content by including the website address in the hosts file
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16,):
		print('Lol! You want to chat now! Its Working time...')
		with open(host_file, 'rt') as file:
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect+""+ website+ "\n")
	# condition to check if current time is not within the working hours and append the content by deleting the website address in the hosts file
	else:
		with open(host_file, 'rt') as file:
			content = file.readlines()
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
				file.truncate()

		print('Social time...')
	time.sleep(5)




