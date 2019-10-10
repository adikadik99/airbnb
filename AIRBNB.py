import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
import logging


driver = webdriver.Chrome(executable_path = "//Users/adik/Downloads/chromedriver")
driver.get("https://www.airbnb.ca/?locale=en&_set_bev_on_new_domain=1568307919_NzEyZGFlNTY5NjQ5")
driver.find_element_by_xpath("//button[@class='optanon-allow-all accept-cookies-button']").click()
driver.find_element_by_xpath("//input[@id='Koan-magic-carpet-koan-search-bar__input']").send_keys("Baku")
driver.implicitly_wait(5)
driver.find_element_by_xpath("//span[contains(text(),'Baku, Azerbaijan')]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'16')]").click()
driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'23')]").click()
driver.find_element_by_xpath("//button[@class='_7ykwo4']").click()

links = driver.find_elements_by_tag_name("a")
print ("Number of links 1: ", len(links))

element = driver.find_element_by_xpath(" //div[@class='_9cfq872']//div//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1] ")
actions = ActionChains(driver)
actions.double_click(element).perform()
driver.find_element_by_xpath("//button[@class='_b0ybw8s']").click()
driver.implicitly_wait(4)
driver.find_element_by_xpath("//span[@class='_ftj2sg4']").click()
driver.get_screenshot_as_file("//Users/adik/Desktop/baku1.png")
driver.implicitly_wait(10)
driver.switch_to.frame
driver.switch_to.frame
driver.switch_to.frame
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("//Users/adik/Desktop/baku2.png")
driver.implicitly_wait(10)
links = driver.find_elements_by_tag_name("a")
print ("Number of links 2: ", len(links))


driver.save_screenshot("////Users/adik/Desktop/baku3.png")

#driver.quit()

'''
class AirBNB():
    def test(self):
        driver = webdriver.Chrome(executable_path="//Users/adik/Downloads/chromedriver")
        driver.get("https://www.airbnb.ca/?locale=en&_set_bev_on_new_domain=1568307919_NzEyZGFlNTY5NjQ5")
        driver.find_element_by_xpath("//button[@class='optanon-allow-all accept-cookies-button']").click()
        driver.find_element_by_xpath("//input[@id='Koan-magic-carpet-koan-search-bar__input']").send_keys("Baku")
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//span[contains(text(),'Baku, Azerbaijan')]").click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'16')]").click()
        driver.find_element_by_xpath("//td[@class='_16zigr23'][contains(text(),'23')]").click()
        driver.find_element_by_xpath("//button[@class='_7ykwo4']").click()

        links = driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))

        element = driver.find_element_by_xpath(
            " //div[@class='_9cfq872']//div//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//button[1] ")
        actions = ActionChains(driver)
        actions.double_click(element).perform()
        driver.find_element_by_xpath("//button[@class='_b0ybw8s']").click()
        driver.implicitly_wait(4)
        driver.find_element_by_xpath("//span[@class='_ftj2sg4']").click()

        links = driver.find_elements_by_tag_name("a")
        print("Number of links present: ", len(links))


        driver.execute_script("window.scrollBy(0,3000)","")

        driver.get_screenshot_as_file("//Users/adik/Desktop/baku2.png")
        driver.quit()
baku = AirBNB()
baku.test()
'''

