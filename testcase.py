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
               
    def test_a1(self): #test case - login with wrong password
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("wrong")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong password.png'))
        print('test case wrong password')
        print('screenshot location is')
        print(Login.save_dir)

    def test_a2(self): #test case - login with wrong email
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@mail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong email address.png'))
        print('test case wrong email')
        print('screenshot location is')
        print(Login.save_dir)

    def test_a3(self): #test case - login with wrong email and password
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@mail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("fail")
        element = driver.find_element_by_id("login-submit").click()
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'wrong emailpassword.png'))        
        print('test case wrong email and password')
        print('screenshot location is')
        print(Login.save_dir)

    def test_a4(self): # test case - login with correct credentials
        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[1]/a").click()
        element = driver.find_element_by_id("emailaddress")
        element.send_keys("kumarants007@gmail.com")
        element = driver.find_element_by_id("password")
        element.send_keys("password")
        element = driver.find_element_by_id("login-submit").click()      
        self.driver.save_screenshot(os.path.join(Login.save_dir, 'correct credentials.png'))
        print('test case correct credentials')
        print('screenshot location is')
        print(Login.save_dir)

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

class Youtube_Voice_Challenge(unittest.TestCase): # to check youtube voice challenge
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\youtube voice challenge\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.challengedip.com')

    def test_e1(self): #test case for youtube voice challenge
        driver = self.driver
        element = driver.find_element_by_link_text('Start the Test').click()
        self.driver.save_screenshot(os.path.join(Youtube_Voice_Challenge.save_dir, "select challenge.png"))
        element = driver.find_element_by_link_text('Youtube Voice Challenge').click()
        self.driver.save_screenshot(os.path.join(Youtube_Voice_Challenge.save_dir, "start here.png"))
        element = driver.find_element_by_id('showbutton').click()
        self.driver.save_screenshot(os.path.join(Youtube_Voice_Challenge.save_dir, "1.png"))
        element = driver.find_element_by_id('ShowAnswer').click()
        self.driver.save_screenshot(os.path.join(Youtube_Voice_Challenge.save_dir, "1answer.png"))
        element = driver.find_element_by_id('ShowURL').click() #1
        driver.implicitly_wait(4) #seconds
        element = driver.find_element_by_id('next')
        self.driver.save_screenshot(os.path.join(Youtube_Voice_Challenge.save_dir, "1video.png"))
        element.click()
        count = 0
        while (count<8):
            element = driver.find_element_by_id('ShowAnswer').click()
            element = driver.find_element_by_id('ShowURL').click()
            element = driver.find_element_by_id('next').click()
            count += 1
        else:
            self.driver.save_screenshot(os.path.join(Youtube_Voice_Challenge.save_dir, "final.png"))
            element = driver.find_element_by_link_text('CHALLENGE DIP').click()
            self.driver.save_screenshot(os.path.join(Youtube_Voice_Challenge.save_dir, "homepage after youtube challenge.png"))
            print('test case Challenge')
            print('screenshot location is')
            print(Youtube_Voice_Challenge.save_dir)

class Cartoon_Challenge(unittest.TestCase): # to check cartoon challenge
    save_dir = 'C:\\Users\\dhamilton\\Desktop\\Selenium project\\output\\cartoon challenge\\'+datetime.now() .strftime("%d-%m-%Y %I-%M %p")
    os.mkdir(save_dir)

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.challengedip.com')
        
    def test_f1(self): #test case for cartoon challenge
        driver = self.driver
        element = driver.find_element_by_link_text('Start the Test').click()
        self.driver.save_screenshot(os.path.join(Cartoon_Challenge.save_dir, "select challenge.png"))
        element = driver.find_element_by_link_text('Cartoon Challenge').click()
        self.driver.save_screenshot(os.path.join(Cartoon_Challenge.save_dir, "start here.png"))
        element = driver.find_element_by_id('showbutton').click()
        self.driver.save_screenshot(os.path.join(Cartoon_Challenge.save_dir, "1.png"))
        element = driver.find_element_by_id('ShowAnswer').click()
        self.driver.save_screenshot(os.path.join(Cartoon_Challenge.save_dir, "1answer.png"))
        element = driver.find_element_by_id('ShowURL').click() #1
        driver.implicitly_wait(4) #seconds
        element = driver.find_element_by_id('next')
        self.driver.save_screenshot(os.path.join(Cartoon_Challenge.save_dir, "1video.png"))
        element.click()
        count = 0
        while (count<8):
            element = driver.find_element_by_id('ShowAnswer').click()
            element = driver.find_element_by_id('ShowURL').click()
            element = driver.find_element_by_id('next').click()
            count += 1
        else:
            self.driver.save_screenshot(os.path.join(Cartoon_Challenge.save_dir, "final.png"))
            element = driver.find_element_by_link_text('CHALLENGE DIP').click()
            self.driver.save_screenshot(os.path.join(Cartoon_Challenge.save_dir, "homepage after cartoon challenge.png"))
            print('test case Cartoon Challenge')
            print('screenshot location is')
            print(Cartoon_Challenge.save_dir)

def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()