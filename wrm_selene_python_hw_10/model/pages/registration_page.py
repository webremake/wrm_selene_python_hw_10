from selene import browser, have, be
from wrm_selene_python_hw_10.resource import path
from wrm_selene_python_hw_10.data.users import User


class RegistrationPage:
    def __init__(self,):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[for^=gender-radio]')
        self.mobile_phone = browser.element('#userNumber')

        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        # self.day_of_birth = browser.element(f'.react-datepicker__day--0{user.day_of_birth}')

        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('[for^=hobbies-checkbox]')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')

        self.state_input = browser.element('#react-select-3-input')
        self.state_options = browser.all('[id^="react-select-3-option"]')

        self.city_input = browser.element('#react-select-4-input')
        self.city_option = browser.all('[id^="react-select-4-option"]')

        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper h5').should(
            have.exact_text('Student Registration Form')
        )

        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('.sidebar-content').execute_script('element.remove()')

        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        return self

    def register(self, user: User):
        self.first_name.should(be.blank).type(user.first_name)
        self.last_name.should(be.blank).type(user.last_name)
        self.email.should(be.blank).type(user.email)
        self.gender.element_by(have.text(user.gender)).click()
        self.mobile_phone.should(be.blank).type(user.mobile_phone)

        self.date_of_birth.click()
        self.month_of_birth.type(user.month_of_birth)
        self.year_of_birth.type(user.year_of_birth)
        # self.day_of_birth.click()
        browser.element(f'.react-datepicker__day--0{user.day_of_birth}').click()

        self.subjects.type(user.subjects).press_enter()
        self.hobbies.element_by(
            have.text(user.hobbies)).should(be.clickable).click()
        self.picture.send_keys(path(user.picture))
        self.current_address.should(be.blank).with_(set_value_by_js=True).set_value(
            user.current_address
        )
        self.state_input.send_keys("a")
        self.state_options.element_by(have.exact_text(user.state)).click()

        self.city_input.send_keys("a")
        self.city_option.element_by(have.exact_text(user.city)).click()

        self.submit_button.with_(click_by_js=True).click()

    def should_have_registered_user_info(self, full_name, email, gender, mobile,
                                         date_of_birth, subjects, hobbies,
                                         picture, address, state_and_city):
        browser.all('.table tbody>tr>td').even.should(have.exact_texts(
            full_name, email, gender, mobile, date_of_birth, subjects,
            hobbies, picture, address, state_and_city))
        return self

    def should_have_registered(self, user: User):
        self.should_have_registered_user_info(
            full_name=f'{user.first_name} {user.last_name}',
            email=user.email,
            gender=user.gender,
            mobile=user.mobile_phone,
            date_of_birth=f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            subjects=user.subjects,
            hobbies=user.hobbies,
            picture=user.picture,
            address=user.current_address,
            state_and_city=f'{user.state} {user.city}'
        )

    def close_thanks_frame(self):
        browser.element('#closeLargeModal').should(be.clickable).click()
        return self
