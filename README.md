# Quora QA Automation
A JavaScript program to use Playwright and GPT-3 to answer questions on Quora. The program uses Playwright to open a Chrome browser and navigate to Quora. The program then extracts the first question listed on Quora and passes it to GPT-3 for a response. The response from GPT-3 is then posted on Quora. This program uses the OpenAI API to access GPT-3.

### Frameworks:

- [Electron](https://www.electronjs.org/)
- [Playwright](https://playwright.dev/)

### Language: 

- JavaScript

### Flow diagrams:

### Requirements:

- [API key](https://beta.openai.com/account/api-keys)

### Modules:
- child_process 
- fs  
- [openai](https://www.npmjs.com/package/openai)
- [selenium-webdriver](https://www.npmjs.com/package/selenium-webdriver)
- sendkeys
- util
- [webdriver_manager](https://www.npmjs.com/package/webdriver-manager)

### API:

- [openai-api](https://openai.com/api/)

### Classes:

### Functions:

1. answer_quora_question(answer): This function is used to post an answer received from GPT-3 on Quora and selecting a personalized answer credential.
2. extract_question(): This function is used to extract the first question listed on www.quora.com/answers and return it as a string.
3. gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['JAX:', 'USER:']): This function is used to ask GPT-3 the question extracted from Quora and return the respone text as a string.
4. launch_test_case(): This function is used to open Quora in a Chrome instance.
5. open_file(filepath): This function is used to open a file and read the contents.
6. quit_application(): This function is used to close the Chrome browser.
7. setup(): This function is used to maximize Chrome window and have the driver wait for 10 seconds.
8. main(): This function is the main method in JavaScript.
9. loop(): This function is used to call the main method in a loop.

### Procedure:

1. Install the required libraries: openai, selenium-webdriver, and chrome.
2. Copy your API key from the OpenAI website.
3. Define Chrome options.
4. Instansiate Google Chrome with the above options. 
5. Create a method to post answer received from GPT-3 on Quora and selecting a personalized answer credential.
6. Create a method to extract the first question listed on www.quora.com/answers and return it as a string.
7. Create a method to ask GPT-3 the question extracted from Quora and return the respone text as a string.
8. Create a method to open Quora in a Chrome instance. 
9. Create a method to open a file and read the contents. 
10. Create a method to close the Chrome browser.
11. Create a setup method to maximize the Chrome window and have the driver wait for 10 seconds.
12. Create a main method to call the above methods.
13. Call the main method in a loop.
### Resources:

1. OpenAI

- [Best Practices for API Key Safety](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)

2. YouTube

- [Build a Desktop App with Electron... But Should You?](https://www.youtube.com/watch?v=3yqDxhR2XxE)

3. Playwright Documentation

- [launch](https://playwright.dev/docs/api/class-browsertype#browser-type-launch)

### Additional notes:


