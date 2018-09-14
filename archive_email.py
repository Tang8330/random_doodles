import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

EMAIL_LINK = ""
USERNAME = ""
PASSWORD = ""

def run():
	driver = webdriver.Chrome()
	driver.get(EMAIL_LINK)
	username = driver.find_element_by_name("j_username")
	username.send_keys(USERNAME)

	password = driver.find_element_by_name("j_password")
	password.send_keys(PASSWORD)

	submit = driver.find_element_by_name("_eventId_proceed")
	submit.click()

	time.sleep(5)
	### Verification Step ###
	verification_button = driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/content/span')
	verification_button.click()
	time.sleep(5)


	# //*[@id=":2a"]/div[1]/span
	while True:
		try:
			checkbox = driver.find_element_by_xpath('//*[@id=":29"]/div[1]/span')
		except Exception:
			checkbox = driver.find_element_by_xpath('//*[@id=":2a"]/div[1]/span')

		checkbox.click()

		time.sleep(2)

		# //*[@id=":5"]/div/div[1]/div[1]/div/div/div[2]/div[1]
		archive_button = driver.find_element_by_xpath('//*[@id=":5"]/div/div[1]/div[1]/div/div/div[2]/div[1]');
		archive_button.click()

		time.sleep(5)
	print("Exiting")

if __name__ == '__main__':
	run()
