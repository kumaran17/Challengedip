import unittest #for writing test case
import os #for mkdir and path
from selenium import webdriver #for selenium to run
from selenium.webdriver.common.keys import Keys #for common functions
from datetime import datetime #for date and time
now = datetime.now()
print(now.strftime("Today's Date is %A %d %B %Y"))
print(now.strftime("And the Time is %I:%M:%S %p"))

class Login(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\login\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_a1(self): #wrong password
        driver = self.driver
        driver.maximize_window()
        self.driver.get('http://www.challengedip.com')
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("wrong")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong password.png'))
        print('screenshot location is')
        print(Login.save_dir)
        print('test case wrong password')

    def test_a2(self): #wrong email
        driver = self.driver
        driver.maximize_window()
        self.driver.get('http://www.challengedip.com')
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@mail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong email address.png'))
        print('test case wrong email')

    def test_a3(self): #wrong email and password
        driver = self.driver
        driver.maximize_window()
        self.driver.get('http://www.challengedip.com')
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@mail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("fail")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong emailpassword.png'))        
        print('test case wrong email and password')

    def test_a4(self): #correct credentials
        driver = self.driver
        driver.maximize_window()
        self.driver.get('http://www.challengedip.com')
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'correct credentials.png'))
        print('test case correct credentials')

class Logout(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\logout\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
                
    def test_b1(self): #to check the logout functionality
        driver = self.driver
        driver.maximize_window()
        self.driver.get('http://www.challengedip.com')
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Logout.save_dir, 'login.png'))
        element = driver.find_element_by_link_text('LOGOUT').click()
        self.driver.save_screenshot(os.path.join(Logout.save_dir, 'logout.png'))
        print('screenshot location is')
        print(Login.save_dir)
        print('test check logout')
    def tearDown(self):
        self.driver.close()

class Contact(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\contact\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_c1(self): #to check the logout functionality
        driver = self.driver
        driver.maximize_window()
        self.driver.get('http://www.challengedip.com')
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Contact.save_dir, 'login.png'))
        self.driver.find_element_by_link_text('CONTACT').click()
        self.driver.save_screenshot(os.path.join(Contact.save_dir, 'contact.png'))
        element = driver.find_element_by_id('firstname').send_keys("test")
        element = driver.find_element_by_id('lastname').send_keys("user")
        element = driver.find_element_by_id('emailaddress').send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id('comment').send_keys("Challenge Dip Website is really a fun place to play with, keep on uploading more contents")
        self.driver.save_screenshot(os.path.join(Contact.save_dir, 'submit form.png'))
        element = driver.find_element_by_id('contact-submit').click()
        self.driver.save_screenshot(os.path.join(Contact.save_dir, 'submitted form.png'))
        print('screenshot location is')
        print(Login.save_dir)
        print('test case contact')

if __name__ == "__main__":
    unittest.main()