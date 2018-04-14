import unittest #for writing test case
import os #for mkdir and path
from selenium import webdriver #for selenium to run
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #explicit wait
from selenium.webdriver.support.ui import WebDriverWait #explicit wait
from selenium.webdriver.support import expected_conditions as EC #explicit wait
from datetime import datetime #for date and time
now = datetime.now()
print(now.strftime("Today's Date is %A %d %B %Y"))
print(now.strftime("And the Time is %I:%M:%S %p"))

class Login(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\login\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.challengedip.com')
               
    def test_a1(self): #wrong password for login
        driver = self.driver
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

    def test_a2(self): #wrong email for login
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@mail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong email address.png'))
        print('test case wrong email')

    def test_a3(self): #wrong email and password for login
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@mail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("fail")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong emailpassword.png'))        
        print('test case wrong email and password')

    def test_a4(self): #correct credentials for login
        driver = self.driver
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
        self.driver.maximize_window()
                
    def test_b1(self): #to check logout
        driver = self.driver
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
        print(Logout.save_dir)
        print('test check logout')

class Contact(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\contact\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_c1(self): #to check contact page
        driver = self.driver
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
        print(Contact.save_dir)
        print('test case contact')

class HomePage(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\homepage\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def test_d1(self): #to check homepage
        driver = self.driver
        self.driver.get('http://www.challengedip.com')
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(HomePage.save_dir, 'login.png'))
        self.driver.find_element_by_link_text('CONTACT').click()
        self.driver.save_screenshot(os.path.join(HomePage.save_dir, 'contact.png'))
        element = driver.find_element_by_link_text("CHALLENGE DIP").click()
        self.driver.save_screenshot(os.path.join(HomePage.save_dir, "homepage after login.png"))
        element = driver.find_element_by_link_text("Start the Test").click()
        driver.implicitly_wait(1)
        element = driver.find_element_by_link_text("Youtube Voice Challenge").click()
        element = driver.find_element_by_id("showbutton").click()
        driver.implicitly_wait(3)
        element = driver.find_element_by_link_text("CHALLENGE DIP").click()
        element = driver.find_element_by_tag_name('h1')
        self.driver.save_screenshot(os.path.join(HomePage.save_dir, "homepage after challenge.png"))
        print('screenshot location is')
        print(HomePage.save_dir)
        print('test case homepage')

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()