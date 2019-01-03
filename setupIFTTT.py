#<!pyhton3>
#Script to configure IFTTT for Smart Home

# *****    pre-requisites before running the script    *****
# *****      Make 1 applet using google assistant      *****

from selenium import webdriver
import time
import getpass

#IFTTT username
user_name = input('\tEnter IFTTT username or email : ')

#IFTTT password
password = getpass.getpass('\tEnter IFTTT password : ')

auth_code = input("\tEnter Blynk auth code : ")

server_address = input('\tEnter server IP address (leave blank if using Blynk cloud server) : ')
if server_address=="" or server_address==" ":
	server_address = '188.166.206.43'
	print("Using blynk cloud server...")

n = int(input("\tEnter number of applets to be created : "))

#eg: 1 2 3 correspons to v_pin = [1,2,3]
v_pin = [str(x) for x in input("\tEnter Virtual pins as a (space-seperated) list : ").split()]

#basic build of Blynk http url
url_build = 'http://' + server_address + '/' + auth_code + '/update/V'

#input from the user for say phrase
say_phrase_input = input('\tEnter say phrase without the command and use "$" as placeholder for numbers\n (eg: "relay $" for relay 1 on, relay 2 on, etc): ')

#say phrase on and off respectively
sp_on = say_phrase_input + ' on'
sp_off = say_phrase_input + ' off'

return_phrase = 'Okay!'

#body text on and off respectively
bt_on = '["1"]'
bt_off = '["0"]'

def new_applet(url, body_text, say_phrase, return_phrase):
	print('Creating applet for "' + say_phrase + '"')
	time.sleep(3)
	while True:
		try:
			new_applet_btn = browser.find_element_by_class_name('new-applet-btn')
			new_applet_btn.click()
			break
		except:
			time.sleep(1)
	#time.sleep(3)
	while True:
		try:
			this_btn=browser.find_element_by_class_name('this-that')
			this_btn.click()
			break
		except:
			time.sleep(1)

	#time.sleep(3)
	while True:
		try:
			google_assistant_tile = browser.find_element_by_partial_link_text('Google Assistant')
			google_assistant_tile.click()
			break
		except:
			time.sleep(1)

	#time.sleep(3)
	while True:
		try:
			say_a_phrase_tile = browser.find_element_by_css_selector('.tanda-selector > ul:nth-child(1) > li:nth-child(1)')
			say_a_phrase_tile.click()
			break
		except:
			time.sleep(1)

	time.sleep(1)
	while True:
		try:
			say_phrase_text = browser.find_element_by_name('fields[voice_input_1]')
			say_phrase_text.send_keys(say_phrase)
			break
		except:
			time.sleep(1)

	time.sleep(1)
	return_phrase_text = browser.find_element_by_name('fields[tts_response]')
	return_phrase_text.send_keys(return_phrase)
	return_phrase_text.submit()

	time.sleep(1)
	while True:
		try:
			this_btn=browser.find_element_by_class_name('this-that')
			this_btn.click()
			break
		except:
			time.sleep(1)
	#time.sleep(3)

	while True:
		try:
			webhooks_tile = browser.find_element_by_partial_link_text('Webhooks')
			webhooks_tile.click()
			break
		except:
			time.sleep(1)

	#time.sleep(3)
	while True:
		try:
			create_btn = browser.find_element_by_css_selector('button.btn')
			create_btn.click()
			break
		except:
			time.sleep(1)

	#time.sleep(3)
	while True:
		try:
			make_webrequest_tile = browser.find_element_by_css_selector('.tanda-selector > ul:nth-child(1) > li:nth-child(1)')
			make_webrequest_tile.click()
			break
		except:
			while True:
				try:
					elem = browser.find_element_by_css_selector('.modal-close > svg:nth-child(1)')
					elem.click()
					break
				except:
					print('trying')

	#time.sleep(3)
	while True:
		try:
			url_field=browser.find_element_by_name('fields[url]')
			url_field.send_keys(url)
			break
		except:
			time.sleep(1)

	time.sleep(1)
	method_box = browser.find_element_by_name('fields[method]')
	method_box.send_keys('PP')
	time.sleep(1)
	content_type_box = browser.find_element_by_name('fields[content_type]')
	content_type_box.send_keys('a')
	time.sleep(1)
	body = browser.find_element_by_name('fields[body]')
	body.send_keys(body_text)
	body.submit()
	time.sleep(4)
	while True:
		try:
			finish_btn = browser.find_element_by_css_selector('input.btn')
			finish_btn.click()
			break
		except:
			time.sleep(1)
	time.sleep(4)
	while True:
		try:
			my_applets = browser.find_element_by_link_text('My Applets')
			my_applets.click()
			break
		except:
			time.sleep(1)

	print("Applet created successfully.")





print("Launching browser window...")
browser = webdriver.Firefox()
browser.get('https://ifttt.com/my_applets')

sign_in_btn =  browser.find_element_by_css_selector('.sign-in')
sign_in_btn.click()

print('Logging in...')
user_name_field = browser.find_element_by_css_selector('#user_username')
user_name_field.send_keys(user_name)

password_field = browser.find_element_by_css_selector('#user_password')
password_field.send_keys(password)
password_field.submit()
print('Logged in successfully.')


for i in range(n):
	new_applet(url_build + v_pin[i], bt_on, sp_on.replace('$', v_pin[i]), return_phrase)
	new_applet(url_build + v_pin[i], bt_off, sp_off.replace('$', v_pin[i]), return_phrase)