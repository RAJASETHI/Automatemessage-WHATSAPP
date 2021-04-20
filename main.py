from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import *
import time
from RandomWordGenerator import RandomWord

rw = RandomWord(max_word_size=5, constant_word_size=False)
lst = rw.getList(num_of_words=50)
# print(lst)
# Should match with the current version of the Web browser
driver = webdriver.Chrome(executable_path=r'C:/chromedriver/chromedriver.exe')

driver.get("https://web.whatsapp.com/")

input("Please Scan QR CODE and press any key to continue: ")
name = input("Enter the Name to whom you want to send the message: ").title()
user = driver.find_element_by_css_selector(f'span[title="{name}"]')
user.click()
# may change inspect->select space -> right click -> copy ->xpath
test_input = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]")
# time.sleep(10)
total_msg = int(input("Enter the Number of messages you want to send: "))
test_input.send_keys("Hello, This is message by raja")
test_input.send_keys(Keys.RETURN)
test_input.send_keys(f"You will be shortly receiving {total_msg} random messages.")
test_input.send_keys(Keys.RETURN)
time.sleep(5)
for i in range(total_msg):
    test_input.send_keys(choice(lst))
    test_input.send_keys(Keys.RETURN)
