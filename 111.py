from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://accounts.google.com")

sleep(1000)