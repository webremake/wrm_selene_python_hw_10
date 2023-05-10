from selene import browser, be, have

from wrm_selene_python_hw_10.data.users import User


class TextBox:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.current_address = browser.element('#currentAddress')
        self.permanent_address = browser.element('#permanentAddress')
        self.output_name = browser.element('#output').element('#name')
        self.output_email = browser.element('#output #email')
        self.output_current_address = browser.element('#output #currentAddress')
        self.output_permanent_address = browser.element('#output #permanentAddress')

    def open(self):
        browser.open('/text-box')
        return self

    def fill_full_name(self, value):
        self.full_name.should(be.blank).type(value)

    def fill_email(self, value):
        self.email.should(be.blank).type(value)

    def fill_current_address(self, value):
        self.current_address.should(be.blank).type(value)

    def fill_permanent_address(self, value):
        self.permanent_address.should(be.blank).type(value)

    def submit(self):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        browser.element('#submit').click()
        return self

    def register(self, user: User):
        self.full_name.should(be.blank).type(user.full_name)
        self.email.should(be.blank).type(user.email)
        self.current_address.should(be.blank).type(user.current_address)
        self.permanent_address.should(be.blank).type(user.current_address)
        self.submit()

    def should_have_data(self, user: User):
        self.output_name.should(have.text(user.full_name))
        self.output_email.should(have.text(user.email))
        self.output_permanent_address.should(have.text(user.current_address))
        self.output_current_address.should(have.text(user.current_address))
