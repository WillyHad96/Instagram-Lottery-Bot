# IMPORTING LIBRARIES
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from string import ascii_lowercase as alphabet
import os
import wget
import time
import string

# CONSTANTS
home_page_url = "https://www.instagram.com/p/C9ShpZcKd0S/"
driver = None
alphabet = 'abcdefghijklmnopqrstuvwxy'
options = Options()
options.add_experimental_option("detach", True)
textarea = None

# FUNCTIONS
def open_chrome():
    global driver
    # OPEN CHROME
    driver = webdriver.Chrome()
    driver.get(home_page_url)
    driver.maximize_window()
    time.sleep(3)

def allow_cookies():
    # ALLOW COOKIES BUTTON
    allow_cookies_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]'))).click()
    time.sleep(1)


def log_in():
    # ENTER CREDENTIALS AND CLICK LOGIN BUTTON
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    password.clear()
    username.send_keys("guillermoteniasmoron@hotmail.com")
    password.send_keys("84264325gtm")
    time.sleep(1)
    sign_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[3]/button"))).click()
    time.sleep(5)

def click_login_button():
    # CLICK LOGIN BUTTON
    log_in_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='_acum'] div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'] div:nth-child(1) a:nth-child(1)"))).click()
    time.sleep(3)

def save_login_info():
    # SAFE INFO BUTTON
    save_info_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mount_0_0_PX']/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/section/div/button"))).click()
    time.sleep(2)
    #XPATH: //*[@id="mount_0_0_a1"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/section/div/button
            #//*[@id="mount_0_0_PX"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/section/div/button
    #CSS SELECTOR: button[type='button']



def click_photo_comment():
    # CLICK PHOTO
    click_photo_coment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".x6s0dn4.x78zum5.x1q0g3np.x1iyjqo2.xs83m0k.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x11njtxf"))).click()
    time.sleep(2)

def add_comment(letter):
    global textarea

    # # CLICK COMMENT
    # comment_section = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_ac"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')))
    # comment_section.click()

    # Locate and interact with the textarea
    textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_FZ"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')))
    textarea.clear()
    textarea.send_keys(Keys.SHIFT, '2')  # SHIFT + 2 is "@" symbol
    textarea.send_keys(letter)
    time.sleep(2)
    return textarea

def send_comment():
    global textarea
    textarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_ac"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[4]/section/div/form/div/textarea')))
    textarea.send_keys(Keys.ENTER) 
    time.sleep(2) 
    textarea.send_keys(Keys.ENTER) 
    time.sleep(2)
    return textarea

def finish_program():
    # FINISH PROGRAM
    driver.quit()


# MAIN PROGRAM
open_chrome()
allow_cookies()
click_login_button()
log_in()
#time.sleep(30)
save_login_info()
for letter in alphabet:
  for i in range(1,4):
    add_comment(letter)
    for j in range(1,i):
      textarea.send_keys(Keys.ARROW_DOWN)
    send_comment()
finish_program()