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

class Contact(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\contact\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.challengedip.com')

    def test_c1(self): #test case for contact page
        driver = self.driver
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
        print('test case contact')
        print('screenshot location is')
        print(Contact.save_dir)

def tearDown(self):
        self.driver.close()
