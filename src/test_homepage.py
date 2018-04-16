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

class HomePage(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\homepage\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.challengedip.com')

    def test_d1(self): #test case for homepage
        driver = self.driver
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
        driver.implicitly_wait(4) #seconds
        element = driver.find_element_by_link_text("Youtube Voice Challenge").click()
        element = driver.find_element_by_id("showbutton").click()
        element = driver.find_element_by_link_text("CHALLENGE DIP").click()
        element = driver.find_element_by_tag_name('h1')
        self.driver.save_screenshot(os.path.join(HomePage.save_dir, "homepage after challenge.png"))
        print('test case homepage')
        print('screenshot location is')
        print(HomePage.save_dir)

def tearDown(self):
        self.driver.close()