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
        self.assertIn("Challenge Dip", driver.page_source)

    def test_a1(self): #test case - login with wrong password
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_class_name("col-sm-4")
        assert element.text == 'Login' , 'login not found'
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("wrong")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong password.png'))
        element = driver.find_element_by_class_name('error-message')
        assert element.text =='Login Error! Please check your Emailaddress and Password.' , 'login error not found'
        print('test case wrong password')
        print('screenshot location is')
        print(Login.save_dir)

    def test_a2(self): #test case - login with wrong email
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_class_name("col-sm-4")
        assert element.text == 'Login' , 'login not found'
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@mail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong email address.png'))
        element = driver.find_element_by_class_name('error-message')
        assert element.text =='Login Error! Please check your Emailaddress and Password.' , 'login error not found'
        print('test case wrong email')
        print('screenshot location is')
        print(Login.save_dir)

    def test_a3(self): #test case - login with wrong email and password
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_class_name("col-sm-4")
        assert element.text == 'Login' , 'login not found'
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@mail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("fail")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong emailpassword.png'))
        element = driver.find_element_by_class_name('error-message')
        assert element.text =='Login Error! Please check your Emailaddress and Password.' , 'login error not found'        
        print('test case wrong email and password')
        print('screenshot location is')
        print(Login.save_dir)

    def test_a4(self): # test case - login with correct credentials
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_class_name("col-sm-4")
        assert element.text == 'Login' , 'login not found'
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()      
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'correct credentials.png'))
        element = driver.find_element_by_class_name("nav-link js-scroll-trigger")
        assert element.text =='Welcome kumaran' , 'welcome name not found'
        print('test case correct credentials')
        print('screenshot location is')
        print(Login.save_dir)

def tearDown(self):
        self.driver.close()