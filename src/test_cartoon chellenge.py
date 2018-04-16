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