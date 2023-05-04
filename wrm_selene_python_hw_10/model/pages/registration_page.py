from selene import browser, have


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.element('.practice-form-wrapper h5').should(have.exact_text('Student Registration Form'))

        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('.sidebar-content').execute_script('element.remove()')


        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
