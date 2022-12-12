# Required libraries
import os
import openai
from requests_html import HTMLSession
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager




class Selenium:
    # Copy your API key from https://beta.openai.com/account/api-keys.
    openai.api_key = "YOURAPIKEY"

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
if __name__ == '__main__':
    conversation = list()
    # Define Chrome options.
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Add a user data directory as an argument for options.
    # Type in "chrome://version/" into your address bar on Chrome and copy the Profile Path as user data directory.
    options.add_argument("--user-data-dir=C:\\Users\\YOURUSERNAME\\AppData\\Local\\Google\\Chrome\\User Data")
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
