import time
import requests

from select import select
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject3/chromedriver.exe')
#driver = webdriver.Edge(executable_path='C:/Users/jagatheswaran.m/PycharmProjects/pythonProject/msedgedriver.exe')
driver.maximize_window()

driver.implicitly_wait(4)
driver.get("https://google.com")
k=driver.find_elements(By.LINK_TEXT, 'a')
print(k)