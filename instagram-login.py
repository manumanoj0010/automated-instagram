from selenium import webdriver
from time import sleep


class App:
    def __init__(self,username='', password='', target_username='', path=''):
        self.username=username
        self.password=password
        self.target_username=target_username
        self.path=path
        self.driver=webdriver.Chrome('C:\Additional Softwares\chromedriver.exe')
        self.main_url='https://www.instagram.com'
        self.driver.get(self.main_url)
        sleep(3)

        self.log_in()

        sleep(3)
        self.driver.close()

    def log_in(self,):
        log_in_button=self.driver.find_element_by_xpath('//div[@class="gr27e"]/p[@class="izU2O"]/a')
        log_in_button.click()
        sleep(3)
        user_name_input=self.driver.find_element_by_xpath('//input[@name="username"]')
        user_name_input.send_keys(self.username)
        password_input=self.driver.find_element_by_xpath('//input[@name="password"]')
        password_input.send_keys(self.password)
        password_input.submit()
        input('submit for now')


if __name__=='__main__':
    app=App()
