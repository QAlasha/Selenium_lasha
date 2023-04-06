from selenium.webdriver.common.by import By


class TexBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # CREATE TexBOX
    FULL_NAME_CREATE = (By.CSS_SELECTOR, '#output #name')
    EMAIL_CREATE = (By.CSS_SELECTOR, '#output #email')
    CURRENT_ADDRESS_CREATE = (By.CSS_SELECTOR, '#output #currentAddress')
    PERMANENT_ADDRESS_CREATE = (By.CSS_SELECTOR, '#output #permanentAddress')


