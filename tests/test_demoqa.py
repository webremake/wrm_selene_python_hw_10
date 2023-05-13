from wrm_selene_python_hw_10.model.pages.registration_page import RegistrationPage
from wrm_selene_python_hw_10.data import users

registration_page = RegistrationPage()


def test_student_registration_form(browser_control):
    # GIVEN
    registration_page.open()

    # WHEN
    registration_page.register(users.student)

    # THEN
    registration_page.should_have_registered(users.student)
    registration_page.close_thanks_frame()
