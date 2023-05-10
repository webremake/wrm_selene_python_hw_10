from wrm_selene_python_hw_10.model.pages.text_box_page import TextBox
from wrm_selene_python_hw_10.data import users


def test_text_box(browser_control):
    # GIVEN
    text_box = TextBox()
    text_box.open()

    # WHEN
    text_box.register(users.student)

    # THEN
    text_box.should_have_data(users.student)
