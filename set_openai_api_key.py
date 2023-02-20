from os import environ
import os

# Define functions to get OpenAI API key from file, environment, or user input.
def get_openai_api_key_from_file(filepath):
    with open(filepath, 'r') as infile:
        return infile.read().strip()

def get_openai_api_key_from_env():
    return os.environ['OPENAI_API_KEY']

def get_openai_api_key_from_user():
    return input("Please enter your OpenAI API key: ")

def set_openai_api_key(api_key):
    # Set the OpenAI API key in the environment variable by using the command line.
    os.system(f"setx OPENAI_API_KEY {api_key}")



# Ask user how they want to enter their OpenAI API key.
def get_openai_api_key():
    while True:
        print("Welcome to the Quora Automation OpenAI API key setup script.")
        print(f"How would you like to enter your OpenAI API key?")
        print("1. From a file")
        print("2. From the environment")
        print("3. From the console")
        print("4. Exit")
        choice = input("Please enter a number: ")
        if choice == '1':
            filepath = input("Please enter the filepath to your API key file: ")
            return get_openai_api_key_from_file(filepath)
        elif choice == '2':
            return get_openai_api_key_from_env()
        elif choice == '3':
            return get_openai_api_key_from_user()
        elif choice == '4':
            exit()
        else:
            print("Invalid choice. Please try again.")



if __name__ == '__main__':
    # Check if the environment variable is already set.
    if "OPENAI_API_KEY" in os.environ:
        print("Your OpenAI API key is already set in the environment.")
        print("You can now run the answering.py script.")
        exit()
    # If the environment variable is not set, ask the user how they want to enter their OpenAI API key.
    else:
        print("Your OpenAI API key is not set in the environment.")
        print("Let's set it now.")
        api_key = get_openai_api_key()
        print("Your OpenAI API key is: %s" % api_key)
        set_openai_api_key(api_key)
        print("Your OpenAI API key has been set in the environment.")
        print("You can now run the answering.py script.")

 