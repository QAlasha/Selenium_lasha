import time

from pages.base_page import BasePage


def test_open_pages(driver):
    page = BasePage(driver, 'https://demoqa.com/')
    page.open()
    time.sleep(3)
