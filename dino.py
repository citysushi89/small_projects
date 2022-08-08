# Automates the Google Dinosaur game

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui

# pull up the website with selenium webdriver
URL = "https://elgoog.im/t-rex/?bot"
s = Service("C:/Users/Owen/Documents/Personal Info/Independent Courses/Python Learning/chromedriver")
chrome_driver_path = "C:/Users/Owen/Documents/Personal Info/Independent Courses/Python Learning/chromedriver"
driver = webdriver.Chrome(service=s)
driver.get(URL)
driver.maximize_window()

# Start the game
pyautogui.keyDown('up')
time.sleep(.5)
pyautogui.keyUp('up')

while True:
    im = pyautogui.screenshot()
    # Blank / white pixel is (247, 247, 247)
    # Check if following pixels are an obstacle
    # Need 2-3 tiers of checking as they can be missed / checks for landing and immediately having to jump
    closest_pixel = im.getpixel((1058, 435))
    farther_pixel = im.getpixel((1069, 430))

    # For testing where the obstacles are
    if closest_pixel != (247, 247, 247):
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')
        print("jumped from close")
    elif farther_pixel != (247, 247, 247):
        pyautogui.keyDown('up')
        pyautogui.keyUp('up')
        print("jumped from middle")

    # Checking if game over and restarting
    game_over_pixel = im.getpixel((1192, 367))
    if game_over_pixel == (83, 83, 83):
        pyautogui.moveTo((1192, 367))
        pyautogui.click()