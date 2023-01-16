# Import required libraries.
import json 
import os
import openai
from requests_html import HTMLSession
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
import time
from time import sleep
import watchdog
from watchdog.observers import Observer
from webdriver_manager.chrome import ChromeDriverManager

# Method to display gui to enter api key and pc user. Then save data to json file.
def api_gui(root):
    # Create main window.
    root.title("Quora Automation")
    root.geometry("400x400")
    
    # Create label and entry box for api key.
    Label(root, text="Enter API Key: ").pack()
    api_key_entry = Entry(root, width=40)
    api_key_entry.pack()
    
    # Create label and entry box for pc user.
    Label(root, text="Enter PC User: ").pack()
    pc_user_entry = Entry(root, width=40)
    pc_user_entry.pack()
    
    # # Create submit button to save api key and pc user to json file and start quora automation.
    # Button(root, text="Submit", command=lambda: [save_data(api_key_entry.get(), pc_user_entry.get()), 
    # root.quit()]).pack()

    Button(root, text="Submit", command=lambda: [save_data(api_key_entry.get(), pc_user_entry.get()), submit(root)]).pack()


def submit(root):
    #close the first GUI 
    root.destroy()

    #create the second GUI window 
    root2 = Tk()

    # Call second gui.
    start_gui(root2)

    

    




# Method to check if data.json exists. If it does, return True. If it doesn't, return False.
def check_json():
    # Check if data.json exists.
    try:
        with open('data.json', 'r') as f:
            # If data.json exists, return True.
            return True
    except:
        # If data.json doesn't exist, return False.  
        return False

# Method to read api key and pc user from json file.

def read_json():
    # Open data.json and read api key and pc user.
    with open('data.json', 'r') as f:
        data = json.load(f)
        # Return api key and pc user.
        return data['api_key'], data['pc_username']

# Method to save api key and pc user to json file.
def save_data(api_key, pc_username):
    # Open data.json and save api key and pc user.
    with open('data.json', 'w') as f:
        # Save api key and pc user to data.json.
        json.dump({'api_key': api_key, 'pc_username': pc_username}, f)

# Method to display gui to start quora automation.
def start_gui(root):
    # Read api key and pc user from json file.
    api_key, pc_username = read_json()

    # Create main window.
    root.title("Quora Automation")
    root.geometry("400x400")
    
    # Create start button to start quora automation and quit gui.
    Button(root, text="Start", command=lambda: [root.quit(), main(api_key, pc_username)]).pack()

    


        




class Selenium:
    # Constructor method. 
    def __init__(self, webdriverval):
        driver = webdriverval

    # Method to post answer received from GPT-3 on Quora and selecting a personalized answer credential.
    def answer_quora_question(self, answer):
        # Click on botton to open answer pop-up.
        answer_popup = self.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div/div[1]/button[1]\
            /div/div[2]/div')
        answer_popup.click()
        # Paste answer into text box.
        answer_box = self.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div')
        answer_box.send_keys(answer)
        # Pause for 10 seconds.
        time.sleep(10)
        # Post answer.
        post = self.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/button')
        post.click()
        # Pause for 2 seconds.
        time.sleep(2)
        # Select "I help people with technology and enjoy learning about ML" as your answer credential. 
        first_answer_credential = self.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/label\
            /div/div[2]/div/span/span[2]')
        # Click on the first answer credential element. 
        first_answer_credential.click()
        


    # Method to extract first question listed on www.quora.com/answers and return it as a string.
    def extract_question(self):
        question = self.find_element(By.XPATH, '//*[@id="mainContent"]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/span/span/a/div/div\
            /div/div/span/span').text
        return question

    # Method to ask GPT-3 the question extracted from Quora and return the respone text as a string.
    def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['JAX:', 'USER:']):
        prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
        response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
        text = response['choices'][0]['text'].strip()
        return text
    
    # Method to open Quora in a Chrome instance. 
    def launch_test_case(self):
        # Open a webpage.
        self.get("https://www.quora.com/answer")
    
    # Method to open a file and read the contents. 
    def open_file(filepath):
        with open(filepath, 'r', encoding='utf-8') as infile:
            return infile.read()

    # Method to close the Chrome browser.
    def quit_application(self):
        # Close the Chrome browser.
        self.quit()

    def setup(self):
        # Maximize Chrome window.
        self.maximize_window()
        # Have the driver wait for 10 seconds. 
        self.implicitly_wait(10)
        self.set_page_load_timeout(20)

    

# Main method in Python.
def main(api_key, pc_username):

    # Set OpenAI API key.
    openai.api_key = api_key
    conversation = list()
    # TODO: Close all Chrome instances before running this script.
    


    # Define Chrome options.
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Add a user data directory as an argument for options.
    # Type in "chrome://version/" into your address bar on Chrome and copy the Profile Path as user data directory.
    options.add_argument("--user-data-dir=C:\\Users\\" + pc_username + "\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("profile-directory=Default")
    # Instansiate Google Chrome with the above options. 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    selenium_client = Selenium
    selenium_client.setup(driver)
    # Pause for 2 seconds.
    time.sleep(2)
    # Create an infinite loop.
    while True:
        selenium_client.launch_test_case(driver)
        # Pause for 2 seconds.
        time.sleep(2)
        question = selenium_client.extract_question(driver)
        answer = selenium_client.gpt3_completion(question)
        selenium_client.answer_quora_question(driver, answer)
        #selenium_client.quit()
