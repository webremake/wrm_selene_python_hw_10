from selene import browser

from wrm_selene_python_hw_10.model.components.panel import MenuPanel
from wrm_selene_python_hw_10.model.pages.text_box_page import TextBox


class Application:
    def __init__(self):
        self.menu_panel = MenuPanel()
        self.text_box = TextBox()

    def open(self):
        browser.open('/elements')
        return self


app = Application()
