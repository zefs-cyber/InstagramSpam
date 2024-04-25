from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
from setting import *
import pandas as pd 
from random import shuffle

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
reciever = 'murod'

links = pd.read_excel('links.xlsx')['post_links'].tolist()
shuffle(links)

# Open Instagram
driver.get("https://www.instagram.com")


def login(username, password):
    username_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = driver.find_element(By.NAME, "password")

    # Fill the login form
    username_input.send_keys(username)  # Replace 'your_username' with your Instagram username
    password_input.send_keys(password)  # Replace 'your_password' with your Instagram password

    submit_form = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
    submit_form.send_keys(Keys.RETURN)

def send_reel(link, username):
    driver.get(link)
    send = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, '_abl-'))
    )
    send.click()
    time.sleep(1.5)

    input_name = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[2]/input'))
    )
    input_name.send_keys(username)
    time.sleep(2)

    select_name = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[1]/div[1]'))
    )
    select_name.click()
    time.sleep(2)

    send_button = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div/div'))
    )
    actions = ActionChains(driver)
    actions.move_to_element(send_button).click().perform()
    print(f'Send clicked - {link}')
    time.sleep(3)

def send_link(link):
    pyautogui.typewrite(link)
    pyautogui.press('enter')

                                            
try:
    login(LOGIN, PASSWORD)
    time.sleep(40)
    for link in links[:200]:
        # send_reel(link, reciever) # slower yet looks better
        # send_link(link) # faster but just copy paste
        time.sleep(1)
    time.sleep(10)
finally:
    # Optional: Close the browser after some operation or keep it open
    driver.quit()