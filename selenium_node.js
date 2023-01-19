// JavaScript source code
// Required libraries
const openai = require('openai');
const {Builder, By, Key, until} = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const fs = require('fs');

// Copy your API key from https://beta.openai.com/account/api-keys.
openai.api_key = "YOURAPIKEY";

// Define Chrome options.
let options = new chrome.Options();
options.addArguments("--user-data-dir=C:\\Users\\YOURUSERNAME\\AppData\\Local\\Google\\Chrome\\User Data");
options.addArguments("profile-directory=Default");

// Instansiate Google Chrome with the above options. 
let driver = new Builder().forBrowser('chrome').setChromeOptions(options).build();

// Method to post answer received from GPT-3 on Quora and selecting a personalized answer credential.
async function answer_quora_question(answer) {
    // Click on botton to open answer pop-up.
    await driver.findElement(By.xpath('//*[@id="mainContent"]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div/div[1]/button[1]\
        /div/div[2]/div')).click();
    // Paste answer into text box.
    await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div[1]/div')).sendKeys(answer);
    // Pause for 10 seconds.
    await driver.sleep(10000);
    // Post answer.
    await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/button')).click();
    // Pause for 2 seconds.
    await driver.sleep(2000);
    // Select "I help people with technology and enjoy learning about ML" as your answer credential. 
    await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/label\
        /div/div[2]/div/span/span[2]')).click();
}

// Method to extract first question listed on www.quora.com/answers and return it as a string.
async function extract_question() {
    let question = await driver.findElement(By.xpath('//*[@id="mainContent"]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/span/span/a/div/div\
        /div/div/span/span')).getText();
    return question;
}

// Method to ask GPT-3 the question extracted from Quora and return the respone text as a string.
async function gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['JAX:', 'USER:']) {
    prompt = prompt.replace(/[^\x00-\x7F]/g, "");
    let response = await openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop
    );
    let text = response['choices'][0]['text'].trim();
    return text;
}

// Method to open Quora in a Chrome instance. 
async function launch_test_case() {
    // Open a webpage.
    await driver.get("https://www.quora.com/answer");
}

// Method to open a file and read the contents. 
async function open_file(filepath) {
    let data = fs.readFileSync(filepath, 'utf8');
    return data;
}

// Method to close the Chrome browser.
async function quit_application() {
    // Close the Chrome browser.
    await driver.quit();
}

async function setup() {
    // Maximize Chrome window.
    await driver.manage().window().maximize();
    // Have the driver wait for 10 seconds. 
    await driver.manage().timeouts().implicitlyWait(10000);
    await driver.manage().timeouts().pageLoadTimeout(20000);
}

// Main method in JavaScript.
async function main() {
    await setup();
    await launch_test_case();
    await driver.sleep(2000);
    let question = await extract_question();
    let answer = await gpt3_completion(question);
    await answer_quora_question(answer);
    //await quit_application();
}

// Call main method in a loop.
(async function loop() {
    while (true) {
        await main();
    }
})();
