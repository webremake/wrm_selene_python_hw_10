from wrm_selene_python_hw_10.model.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_student_registration_form(browser_control):
    # GIVEN
    registration_page.open()

    # WHEN
    registration_page\
        .fill_first_name('Jon').fill_last_name('Dir')\
        .fill_email('jondir@example.com')\
        .select_gender('Male')\
        .fill_mobile_phone('5296846163')\
        .fill_date_of_birth('1957', 'May', '12')\
        .fill_subjects('Commerce')\
        .select_hobbies('Reading')\
        .upload_picture('gl.jpg')\
        .fill_current_address('This is my current address in New York USA')\
        .select_state('Haryana').select_city('Karnal')\
        .submit()

    # THEN
    registration_page\
        .should_thanks_frame_have_title('Thanks for submitting the form')\
        .should_thanks_frame_table_have_columns(2)\
        .should_thanks_frame_table_have_header_sells('Label', 'Values')\
        .should_thanks_frame_table_have_rows(10)\
        .should_have_registered_user_info(
            'Jon Dir',
            'jondir@example.com',
            'Male',
            '5296846163',
            '12 May,1957',
            'Commerce',
            'Reading',
            'gl.jpg',
            'This is my current address in New York USA',
            'Haryana Karnal')\
        .close_thanks_frame()
