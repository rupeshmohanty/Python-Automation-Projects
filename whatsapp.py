from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("http://web.whatsapp.com/")

input("Please scan the qr code and press any key to continue!")

user = driver.find_element_by_css_selector('span[title="Trideep Sensei"]')
user.click()

testinput = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

time.sleep(10)
testinput.send_keys("Hey!This message is an automated message using Python")
testinput.send_keys(Keys.RETURN)