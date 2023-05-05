from selene import browser, have, be

from wrm_selene_python_hw_10.resource import path


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper h5').should(
            have.exact_text('Student Registration Form')
        )

        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('.sidebar-content').execute_script('element.remove()')

        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, address):
        browser.element('#userEmail').should(be.blank).type(address)

    def select_gender(self, value):
        browser.all('[for^=gender-radio]').element_by(have.text(value)).click()

    def fill_mobile_phone(self, number):
        browser.element('#userNumber').should(be.blank).type(number)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, text):
        browser.element('#subjectsInput').type(text).press_enter()

    def select_hobbies(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(
            have.text(value)).should(be.clickable).click()

    def upload_picture(self, file):
        browser.element('#uploadPicture').send_keys(path(file))

    def fill_current_address(self, text):
        browser.element('#currentAddress').should(be.blank).with_(set_value_by_js=True).set_value(
            text
        )

    def select_state(self, name):
        browser.element('#react-select-3-input').send_keys("a")
        browser.all('[id^="react-select-3-option"]').element_by(
            have.exact_text(name)
        ).click()

    def select_city(self, name):
        browser.element('#react-select-4-input').send_keys("a")
        browser.all('[id^="react-select-4-option"]').element_by(
            have.exact_text(name)
        ).click()

    def submit(self):
        browser.element('#submit').with_(click_by_js=True).click()
