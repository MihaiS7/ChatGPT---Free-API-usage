from selenium.webdriver.common.by import By


class Locators():
    """ Selenium locators """

    LOG_IN = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[1]/div/div/button[1]/div')
    EMAIL_ADDRESS = (By.ID, "username")
    CONTINUE = (By.CSS_SELECTOR, "button[value='default']")
    PASSWORD = (By.ID, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@class='c320322a4 c480bc568 c20af198f ce9190a97 _button-login-password']")
    
    ACCEPTING_REQUIREMENTS = (By.XPATH, "//*[@id='radix-:r9:']/div[2]/div[2]/div/button[1]/div")
    FIRST_SECOND_BUTTON = (By.XPATH, "//div[@class='p-4 sm:p-6 sm:pt-4']//button[contains(@class, 'btn relative btn-neutral ml-auto')]")
    DONE_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-primary')]/div[contains(text(), 'Done')]")

class MessagePageLocator():
    SEND_MESSAGE_BOX = (By.ID, "prompt-textarea")
    SEND_MESSAGE_BUTTON = (By.XPATH, "//button[contains(@class, 'absolute p-1 rounded-md md')]")
    CONTINUE_GENERATING = (By.XPATH, "//button[contains(@class, 'btn relative btn-neutral border-0 md:border')]")

class OutputMessage():
    OUTPUT_MESSAGE_BOX = (By.XPATH, "//div[contains(@class, 'markdown prose w-full break-words dark:prose-invert light')]")

class Errors():
    REGENERATE_RESPONSE = (By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div/main/form/div[2]/button')
    GENERATED_ERROR = (By.XPATH, "//div[contains(@class, 'mb-3 text-center text-xs') and contains(text(), 'Done')]")