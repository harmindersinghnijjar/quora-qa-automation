# quora-qa-automation
This is an object oriented code template for a bot that will eventually answer questions on Quora using the OpenAI API and Selenium.

### Language: 

- Python

### Flow diagrams:

### Requirements:

- [API key](https://beta.openai.com/account/api-keys)

### Libraries:

- OpenAI
- os
- Selenium
- webdriver_manager

### API:

- [~~quora-api~~](https://github.com/csu/quora-api)
- [openai-api](https://openai.com/api/)

### Classes:

- Selenium

### Functions:

1. def answer_quora_question(self, answer)
2. def extract_question(self)
3. def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['JAX:', 'USER:'])
4. def launch_test_case(self)
5. def open_file(filepath)
6. def quit_application(self)
7. def setup(self)

### Procedures:

1. Open Quora in a Chrome instance that already has user data on it.
2. Go to "[https://www.quora.com/answer](https://www.quora.com/answer)" and extract the first question.
3. Asks GPT-3 for the answer to the question.
4. Post the answer into Quora.
5. Change the answer credentials to your preferred credentials.

### Resource:

1. YouTube:

[https://www.youtube.com/watch?v=bpacnzHwQGo](https://www.youtube.com/watch?v=bpacnzHwQGo)

[https://www.youtube.com/watch?v=ePdmv4ucmb8](https://www.youtube.com/watch?v=ePdmv4ucmb8)

1. Stack overflow

[Python: Selenium write in the text box of a form](https://stackoverflow.com/questions/33062149/python-selenium-write-in-the-text-box-of-a-form)

### Additional notes:

Note: Change lines 17 and 100 of v1.py to the proper API key and path to your Google Chrome profile respectively
