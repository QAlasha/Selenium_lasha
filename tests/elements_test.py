
from pages.elements_page import TexBoxPage


class TestElements:
    class TestTexBox:

        def test_tex_box(self, driver):
            text_box_page = TexBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_field()
