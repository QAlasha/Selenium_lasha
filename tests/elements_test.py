from pages.elements_page import TexBoxPage


class TestElements:
    class TestTexBox:

        def test_tex_box(self, driver):
            text_box_page = TexBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_field()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_field_form()
            print(output_name)
            print(output_email)
            print(output_cur_addr)
            print(output_per_addr)
