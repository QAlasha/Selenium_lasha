import time

from pages.base_page import BasePage
from locators.elements_page_locators import TexBoxPageLocators


class TexBoxPage(BasePage):
    locators = TexBoxPageLocators

    # заполняем все поля
    def fill_all_field(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('Baslandze')
        self.element_is_visible(self.locators.EMAIL).send_keys('QA_lasha@mail.ru')
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys('Moscow')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('Klin')
        self.go_to_footer(self.locators.FOOTER)
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(5)

    def check_field_form(self):
        full_name = self.element_is_present(self.locators.FULL_NAME_CREATE).text
        email = self.element_is_present(self.locators.EMAIL_CREATE).text
        current_address = self.element_is_present(self.locators.CURRENT_ADDRESS_CREATE).text
        permanent_address = self.element_is_present(self.locators.PERMANENT_ADDRESS_CREATE).text
        return full_name, email, permanent_address, current_address