from selene import browser, have
from wrm_selene_python_hw_10.model.pages.text_box_page import TextBox
from wrm_selene_python_hw_10.data import users

def test_text_box(browser_control):
    # GIVEN
    text_box = TextBox()
    text_box.open()

    # WHEN
    text_box.register(users.student)

    # THEN
    browser.element('#output #name').should(have.text(users.student.full_name))
    browser.element('#output #email').should(have.text(users.student.email))
    browser.element('#output #currentAddress').should(have.text(users.student.current_address))
    browser.element('#output #permanentAddress').should(have.text(users.student.current_address))
