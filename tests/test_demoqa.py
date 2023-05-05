from selene import browser, have, be

from wrm_selene_python_hw_10.model.pages.registration_page import RegistrationPage

def test_student_registration_form(browser_control):
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Jon')
    registration_page.fill_last_name('Dir')
    registration_page.fill_email('jondir@example.com')
    registration_page.select_gender('Male')
    registration_page.fill_mobile_phone('5296846163')
    registration_page.fill_date_of_birth('1957', 'May', '12')
    registration_page.fill_subjects('Commerce')
    registration_page.select_hobbies('Reading')
    registration_page.upload_picture('gl.jpg')
    registration_page.fill_current_address('This is my current address in New York USA')
    registration_page.select_state('Haryana')
    registration_page.select_city('Karnal')
    registration_page.submit()

    # THEN
    # section CHECK IFRAME TABLE
    # check table header has two columns
    browser.all('.table thead>tr>th').should(have.size(2))

    # check table header cells have correct text
    browser.all('.table thead>tr>th').should(have.exact_texts('Label', 'Values'))

    # check table body has ten columns
    browser.all('.table tbody>tr').should(have.size(10))

    # check table cells in column Value have values entered into the form in the previous steps
    browser.all('.table tbody>tr>td').even.should(have.exact_texts(
        'Jon Dir', 'jondir@example.com', 'Male', '5296846163', '12 May,1957', 'Commerce',
        'Reading', 'gl.jpg', 'This is my current address in New York USA', 'Haryana Karnal'))
    # end section

    # close iframe table
    browser.element('#closeLargeModal').should(be.clickable).click()