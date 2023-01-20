// TODO - Add comments to code.
// TODO - Add Mac support.
// TODO - Add error handling to code.
// TODO - Add logging to code.
// TODO - Send answer to Quora using Selenium, not sendkeys.
// TODO - Implement UI for user to enter pc username for Chrome profile.


// DONE - write function requireAll() to mention required libraries in a neat and understandable way. 
// Method to require all libraries in one line.
const requireAll = (modules) => {
    const requiredModules = {};
    modules.forEach(module => {
        requiredModules[module] = require(module);
    });
    return requiredModules;
}

// Import required libraries.
const requiredModules = requireAll(['child_process', 'fs', 'openai', 'selenium-webdriver', 'selenium-webdriver/chrome', 'sendkeys', 'util']);

console.log('Importing required libraries...');

// Destructure required libraries.
const {
    exec,
    fs,
    Configuration,
    OpenAIApi,
    Builder,
    By,
    Key,
    until,
    chrome,
    SendKeys,
    util
} = requiredModules;

console.log('Destructuring required libraries...');

// Write required libraries to log file.
try {
    fs.writeFile('log.txt', util.inspect(requiredModules, {
        depth: null
    }), (err) => {
        if (err) {
            console.log(err);
        }
    });
} catch (err) {
    console.log(err);
}

console.log('Starting script...');

// // Create a new OpenAI API configuration.
// const configuration = new Configuration({
//     apiKey: process.env.OPENAI_API_KEY,
// });

// // Uncomment the below line to log the API key.
// //console.log(configuration.apiKey)

// // Create a new OpenAI API instance.
// const openai = new OpenAIApi(configuration);

// //TODO - Add method to check if OS is Windows or Mac.
// // TODO - Add Mac support.
// // Close all open Chrome instances before running the script.
// // Windows
// exec('taskkill /f /im chrome.exe', (err, stdout, stderr) => {
//     if (err) {
//         console.log(err);
//     }
//     console.log(stdout);
// });

// // Define Chrome options.
// let options = new chrome.Options();
// options.addArguments("--user-data-dir=C:\\Users\\harmi\\AppData\\Local\\Google\\Chrome\\User Data");
// options.addArguments("profile-directory=Default");

// // Instansiate Google Chrome with the above options. 
// let driver = new Builder().forBrowser('chrome').setChromeOptions(options).build();

// // Method to post answer received from GPT-3 on Quora and selecting a personalized answer credential.
// async function answer_quora_question(answer) {
//     // Click on botton to open answer pop-up.
//     await driver.findElement(By.xpath('/html/body/div[2]/div/div[2]/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div[1]/button[1]')).click();
//     // Pause for 5 seconds.
//     await driver.sleep(5000);
//     // Click on text box to enter answer.
//     // TODO - Ensure driver is clicking on the correct text box.
//     // TODO - Send answer to Quora using Selenium, not sendkeys.
//     await driver.findElement(By.className('doc empty')).click();
//     await driver.findElement(By.className('doc empty')).clear();
//     // Paste answer into text box.
//     await sendkeys(answer);

//     // Pause for 10 seconds.
//     await driver.sleep(10000);
//     // Post answer.
//     await driver.findElement(By.xpath('/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div/div[2]/button')).click();
//     // Pause for 2 seconds.
//     await driver.sleep(2000);
//     // TODO - Make this more robust.
//     // Select "I help people with technology and enjoy learning about ML" as your answer credential. 
//     await driver.findElement(By.xpath('//*[@id="root"]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/label/div/div[2]/div/span/span[2]')).click();
// }

// // Method to extract first question listed on www.quora.com/answers and return it as a string.
// async function extract_question() {
//     let question = await driver.findElement(By.xpath('//*[@id="mainContent"]/div/div/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/span/span/a/div/div/div/div/span/span')).getText();
//     // Logging the question to the console causes the script to crash whenever the question contains a special character.
//     //console.log(question);
//     return question;
// }

// // Method to ask GPT-3 the question extracted from Quora and return the respone text as a string.
// async function gpt3_completion(prompt, model = 'text-davinci-003', temp = 0.7, top_p = 1.0, tokens = 400, freq_pen = 0.0, pres_pen = 0.0, stop = ['JAX:', 'USER:']) {
//     prompt = prompt.replace(/[^\x00-\x7F]/g, "");
//     const response = await openai.createCompletion({
//         model: model,
//         prompt: prompt,
//         temperature: temp,
//         max_tokens: tokens,
//         top_p: top_p,
//         frequency_penalty: freq_pen,
//         presence_penalty: pres_pen,
//         stop: stop
//     });
//     let text = response.data.choices[0].text;
//     // Remove spaces from the beginning of the string.
//     text = text.replace(/^\s+/, '');
//     return text;

// }

// // Method to open Quora in a Chrome instance. 
// async function launch_test_case() {
//     // Open a webpage.
//     await driver.get("https://www.quora.com/answer");
// }

// // Method to close the Chrome browser.
// async function quit_application() {
//     // Close the Chrome browser.
//     await driver.quit();
// }

// async function setup() {
//     // Maximize Chrome window.
//     await driver.manage().window().maximize();
//     // Have the driver wait for 10 seconds. 
//     await driver.sleep(10000);
// }

// // Main method in JavaScript.
// async function main() {
//     // Setup Chrome instance.
//     await setup();
//     // Open Quora.
//     await launch_test_case();
//     // Pause for 2 seconds.
//     await driver.sleep(2000);
//     // Extract question from Quora.
//     let question = await extract_question();
//     // Ask GPT-3 the question.
//     let answer = await gpt3_completion(question);
//     // Post answer on Quora.
//     await answer_quora_question(answer);
//     // Close Chrome instance.
//     //await quit_application();
// }

// // Call main method in a loop.
// (async function loop() {
//     // TODO - Add a break condition to the loop.
//     // TODO - Add a delay between each iteration of the loop.
//     while (true) {
//         // Call main method.
//         await main();
//     }
// })();