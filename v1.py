from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

class Selenium:

    def __init__(self, webdriverval):
        driver = webdriverval
        
    
    def setup(self):
        # Maximize Chrome window.
        self.maximize_window()
        # Have the driver wait for 10 seconds. 
        self.implicitly_wait(10)
        self.set_page_load_timeout(20)

    
    def launch_test_case(self):
        # Open a webpage.
        self.get("https://www.quora.com")
        

    def quit_application(self):
        # Close the Chrome browser.
        self.quit()

# Main method in Python.
if __name__ == '__main__':
    # Define Chrome options.
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Add a user data directory as an argument for options.
    # Type in "chrome://version/" into your address bar on Chrome and copy the Profile Path as user data directory.
    options.add_argument("--user-data-dir=C:\\Users\\Harminder Nijjar\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("profile-directory=Default")
    # Instansiate Google Chrome with the above options. 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    selenium_client = Selenium
    selenium_client.setup(driver)
    selenium_client.launch_test_case(driver)
    #selenium_client.quit()