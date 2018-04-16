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

class Logout(unittest.TestCase):
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\logout\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.challengedip.com')

    def test_b1(self): #test case for logout
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Logout.save_dir, 'login.png'))
        element = driver.find_element_by_link_text('LOGOUT').click()
        self.driver.save_screenshot(os.path.join(Logout.save_dir, 'logout.png'))
        print('test check logout')
        print('screenshot location is')
        print(Logout.save_dir)

def tearDown(self):
        self.driver.close()