from selenium import webdriver
from confidential import username,password

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def github(self):
        self.driver.get('https://github.com/')

        # clicks on the login button
        login = self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
        login.click()

        # clicks and inputs in the username field
        uname = self.driver.find_element_by_xpath('//*[@id="login_field"]')
        uname.click()
        uname.send_keys(username)

        # clicks and inputs in the password field
        pwd = self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.click()
        pwd.send_keys(password)

        # click the login button
        button = self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[12]')
        button.click()

bot = Bot()
bot.github()