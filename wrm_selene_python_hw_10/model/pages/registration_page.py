from selene import browser, have, be

from wrm_selene_python_hw_10.resource import path


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        # browser.element('.practice-form-wrapper h5').should(
        #     have.exact_text('Student Registration Form')
        # )

        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('.sidebar-content').execute_script('element.remove()')

        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, address):
        browser.element('#userEmail').type(address)
        return self

    def select_gender(self, value):
        browser.all('[for^=gender-radio]').element_by(have.text(value)).click()
        return self

    def fill_mobile_phone(self, number):
        browser.element('#userNumber').type(number)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, text):
        browser.element('#subjectsInput').type(text).press_enter()
        return self

    def select_hobbies(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(
            have.text(value)).should(be.clickable).click()
        return self

    def upload_picture(self, file):
        browser.element('#uploadPicture').send_keys(path(file))
        return self

    def fill_current_address(self, text):
        browser.element('#currentAddress').should(be.blank).with_(set_value_by_js=True).set_value(
            text
        )
        return self

    def select_state(self, name):
        browser.element('#react-select-3-input').send_keys("a")
        browser.all('[id^="react-select-3-option"]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def select_city(self, name):
        browser.element('#react-select-4-input').send_keys("a")
        browser.all('[id^="react-select-4-option"]').element_by(
            have.exact_text(name)
        ).click()
        return self

    def submit(self):
        browser.element('#submit').with_(click_by_js=True).click()
        return self

    def should_thanks_frame_have_title(self, text):
        browser.element('.modal-header').should(have.text(text))
        return self

    def should_thanks_frame_table_have_columns(self, column_number: int):
        browser.all('.table thead>tr>th').should(have.size(column_number))
        return self

    def should_thanks_frame_table_have_header_sells(self, sell1, sell2):
        browser.all('.table thead>tr>th').should(have.exact_texts(sell1, sell2))
        return self

    def should_thanks_frame_table_have_rows(self, rows_number: int):
        browser.all('.table tbody>tr').should(have.size(rows_number))
        return self

    def should_have_registered_user_info(self, full_name, email, gender, mobile,
                                         date_of_birth, subjects, hobbies,
                                         picture, address, state_and_city):
        browser.all('.table tbody>tr>td').even.should(have.exact_texts(
            full_name, email, gender, mobile, date_of_birth, subjects,
            hobbies, picture, address, state_and_city))
        return self

    def close_thanks_frame(self):
        browser.element('#closeLargeModal').should(be.clickable).click()
        return self
