from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://vc.farspnu.ac.ir/Student/HomeWork')

def Login():
    username = driver.find_element(By.ID, 'Input_UserName')
    password = driver.find_element(By.ID, 'password')
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    
    username.send_keys('401956553')
    password.send_keys('2420946596aA')
    login_button.click()

def CheckHomework():
    homeworks_link = driver.find_element(By.XPATH, "//a[@href='/Student/HomeWork']")
    homeworks_link.location_once_scrolled_into_view
    homeworks_link.click()

Login()
CheckHomework()