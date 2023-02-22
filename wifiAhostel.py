from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os
import subprocess
os.system('cmd /c "netsh wlan show networks"')

name_of_router = 'BPGC-A_HOSTEL'
os.system(f'''cmd /c "netsh wlan connect name={name_of_router}"''')
###########################################################
#for choosing wifi:


#enter the link to the website you want to automate login.
website_link="https://campnet.bits-goa.ac.in:8090/httpclient.html"
#enter your login username
username="f20201949"
#enter your login password
password="alto2126"

###########################################################

#enter the element for username input field
element_for_username="username"
#enter the element for password input field
element_for_password="password"
#enter the element for submit button
element_for_submit="loginbutton"

###########################################################

#browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())	#for Firefox user
#browser = webdriver.Safari()	#for macOS users[for others use chrome vis chromedriver]
browser = webdriver.Chrome()	#uncomment this line,for chrome users
browser.get((website_link))

#username_element = browser.find_element("name", "username")
#print("done")
#username_element.send_keys(username)
#password_element = browser.find_element("name", "password")
#password_element.send_keys(password)
#signInButton = browser.find_element("id", "loginbutton")

#signInButton.click()
try:
	
	username_element = browser.find_element("name", "username")
	username_element.send_keys(username)
	password_element = browser.find_element("name", "password")
	password_element.send_keys(password)
	signInButton = browser.find_element("id", "loginbutton")

	signInButton.click()
	
	#### to quit the browser uncomment the following lines ####
	time.sleep(1)
	browser.quit()
	#time.sleep(1)
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)
except Exception:
	#### This exception occurs if the element are not found in the webpage.
	print("Some error occured :(")

	#### to quit the browser uncomment the following lines ####
	# browser.quit()
	# browserExe = "Safari"
	# os.system("pkill "+browserExe)