from selenium import webdriver
from confidential import username,password

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
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
    
    def newRepo(self):
        self.driver.get('https://github.com/new')
        repo = input("Enter your repository name: ")
        description = input("Enter your repository description: ")

        # Input repo name
        repoName = self.driver.find_element_by_xpath('//*[@id="repository_name"]')
        repoName.click()
        repoName.send_keys(repo)

        # Input repo description
        repoDes = self.driver.find_element_by_xpath('//*[@id="repository_description"]')
        repoDes.click()
        repoDes.send_keys(description)

        # Create a public repo 
        public = self.driver.find_element_by_xpath('//*[@id="repository_visibility_public"]')
        public.click()

        # select to add a readme file
        checkBox = self.driver.find_element_by_xpath('//*[@id="repository_auto_init"]')
        checkBox.click()

        # create repo
        create = self.driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
        create.submit()

if __name__ == "__main__":
    github = Bot()
    github.login()
    github.newRepo()