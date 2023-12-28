print("--------- The script just began --------")


import csv
import time

import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators import Errors, Locators, MessagePageLocator, OutputMessage
import creating_env_file

URL = "https://chat.openai.com/auth/login"
# CHROME_TARGET_VERSION = 114

# Login credentials
if __name__=='__main__':
    file_name = "credentials.dev"
    username, password = creating_env_file.writing_file(file_name=file_name)
print(username)
print(password)
# Initialize the Chrome driver
driver = uc.Chrome()
driver.get(URL)


def to_login():
    print("Your data will be passed in locators for log in. \n")
    login_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((Locators.LOG_IN))
    )
    login_button.click()
    time.sleep(5)

    username_section = driver.find_element(*Locators.EMAIL_ADDRESS)
    username_section.send_keys(username)

    continue_button = driver.find_element(*Locators.CONTINUE)
    continue_button.click()
    time.sleep(2)

    password_section = driver.find_element(*Locators.PASSWORD)
    password_section.send_keys(password)

    login_submit = driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON)
    driver.execute_script("arguments[0].click();", login_submit)

    print("\nSuccessful login. You are into your account!\n")


def accept_requirements():
    try:
        accepting_requirements = driver.find_element(*Locators.ACCEPTING_REQUIREMENTS)
        accepting_requirements.click()
    except NoSuchElementException:
        pass

    while True:
        try:
            next_buttons = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located(Locators.FIRST_SECOND_BUTTON)
            )
            for button in next_buttons:
                if button.text == "Next":
                    button.click()
                    time.sleep(2)
                    break
        except (NoSuchElementException, TimeoutException):
            break

    try:
        done_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.DONE_BUTTON)
        )
        if done_button:
            done_button.click()
    except (NoSuchElementException, TimeoutException):
        print("Couldn't find the Done button.")

    print("\nThe requirements were accepted.\n")

def chat():
    with open("prompt_gpt.csv", "r") as file:
        csvreader = csv.reader(file, delimiter=";")
        messages_csvreader = list(csvreader)
        messages = []
        for row in messages_csvreader:
            messages.extend(row)
        result = [message for message in messages if message.split()]
        print(f"These are the inputs: {result}")

    
    output_queue = []
    max_iterations = len(messages)
    iteration = 0

    for i in range(len(result)):
        if iteration >= max_iterations:
            break
        if (i % 4) == 0 and i >= 4:
            message = ''.join(output_queue[i-2]) + " " + ''.join(result[i-1])
            # print(f"This is the full message: {message}")
            # print(f"This is the result[i-1]: {result[i-1]}")
        else:
            message = result[i]
        # print(f"Using message: {message}")

        time.sleep(12)
        sending_messages_box = driver.find_element(*MessagePageLocator.SEND_MESSAGE_BOX)
        try:
            button_send_messages = driver.find_element(*MessagePageLocator.SEND_MESSAGE_BUTTON)
            message = ''.join(message)
            for character in message.replace('\n', ' '):
                sending_messages_box.send_keys(character)
                time.sleep(0.02)
            time.sleep(5)
            button_send_messages.click()
        except NoSuchElementException:
            try:
                regenerate_button = driver.find_element(*Errors.REGENERATE_RESPONSE)
                print("In case you encountered some issues in generating the response, I am here to handle the error!")
                if regenerate_button:
                    print(
                    "There is an error with generating response, please wait until I'm trying to fix that!😵")
                    regenerate_button.click()
            except NoSuchElementException:
                pass

        old_output = "" 
        while True:
            time.sleep(5)
            output_messages = driver.find_elements(*OutputMessage.OUTPUT_MESSAGE_BOX)
            new_output = output_messages[-1].text
            if new_output != old_output:
                print(f"Output: {new_output}")
                old_output = new_output 
            else:
                output_queue.append(old_output) 
                break
        
        try:
            continue_generating = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located(MessagePageLocator.CONTINUE_GENERATING)
            )
            if continue_generating:
                continue_generating.click()
                print(
                "\n'Continue Generating' button is searching.")
                # WebDriverWait(driver, 5).until(
                #     EC.element_to_be_clickable(MessagePageLocator.SEND_MESSAGE_BUTTON)
                # )
                print(
                    "The button was clicked, it will generate more content for this message."
                )
            else:
                pass
        except (NoSuchElementException, TimeoutException):
            pass

        while True:
            time.sleep(5)
            output_messages = driver.find_elements(*OutputMessage.OUTPUT_MESSAGE_BOX)
            new_output = output_messages[-1].text
            if new_output != old_output:
                old_output = new_output 
            else:
                break

    with open("output_results.csv", "a", newline="", encoding="utf-8") as output_file:
        headers=['Output 1', 'Output 2', 'Output 3', 'Output 4']
        writer = csv.DictWriter(output_file, headers)
        
        if output_file.tell() == 0:
            writer.writeheader()

        for i in range(0, len(output_queue), 4):
            writer.writerow({'Output 1': output_queue[i] if i < len(output_queue) else None,
                                'Output 2': output_queue[i+1] if i+1 < len(output_queue) else None,
                                'Output 3': output_queue[i+2] if i+2 < len(output_queue) else None,
                                'Output 4': output_queue[i+3] if i+3 < len(output_queue) else None,
                            })
        
        output_queue = []
        iteration +=1
        
asking_data = print("""Hi, because of the sensitive details,
      I would like to ask you to add your login credentials
      here.""")
    
to_login()
time.sleep(5)
accept_requirements()
time.sleep(8)
chat()
driver.quit()
