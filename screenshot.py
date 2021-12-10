#makes a screenshot of a website
import pyautogui
import time
import webbrowser
import datetime
from datetime import datetime
import os

initial_count = 0
dir = "screenshots"

for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        initial_count += 1

def start():   #start
    number = initial_count  #number of screenshots based on number of screenshot images

    for i in range(5):  #prints kill switch message 5 times
        print("TO STOP PROGRAM, PUT MOUSE CURSOR IN THE TOP CORNER OF YOUR SCREEN")  #kill switch message

    websiteInputQ = input("Website url without https:// (example: google.com   ")  #website to open. without "https://" to name file
    websiteInput = "https://"+websiteInputQ  #adds the "https://" to open website
    secondsWait = input("Seconds between refresh   ")  #seconds between the screenshots

    webbrowser.open_new_tab(websiteInput)  #opens the website

    for i in range(1000000000):  #loops "forever" 
        time.sleep(int(secondsWait))  #waits the seconds you chose
        number = number + 1  #makes the number go up with 1 every screenshot

        now = datetime.now()  #todays date 
        dt_string = now.strftime("%d,%m,%Y_%H,%M,%S")  #todays date but better

        screenshot = pyautogui.screenshot()  #takes screenshot
        screenshot.save(r'screenshots\screenshot'+ str(number) + '.png')  #saves the screenshot in folder
        
        print("Took a new screenshot")  #tell you it took the screenshot
        print("I have now got  "+ str(number) +"  screenshots")  #tell you how many screenshots you have

        pyautogui.press("f5")  #refreshes the page


start()  #runs "start"
