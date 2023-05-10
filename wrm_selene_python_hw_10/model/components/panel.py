from selene import browser, have
from wrm_selene_python_hw_10.model.pages.text_box_page import TextBox


class MenuPanel:
    def __init__(self):
        self.panel_container = browser.element('.left-panel')
        self.panel_menu_item_texts = browser.element('.left-pannel').all('.menu-list .text')

    def open_panel_menu_item(self, link_text: str):
        # browser.open('/elements')
        self.panel_menu_item_texts.element_by(have.exact_text(link_text)).click()
        return TextBox

    def open_text_box(self):
        self.open_panel_menu_item('Text Box')
        return TextBox
