from selene import browser, have, be
from wrm_selene_python_hw_10.data import users


def test_text_box():
    # GIVEN
    browser.open('/text-box')

    # Remove advertising banners
    browser.execute_script('document.querySelector("#fixedban").remove()')
    # browser.element('footer').execute_script('element.remove()')
    browser.element('.sidebar-content').execute_script('element.remove()')

    # WHEN
    browser.element('#userName').should(be.blank).type(f'{users.student.first_name} {users.student.last_name}')
    browser.element('#userEmail').should(be.blank).type(users.student.email)
    browser.element('#currentAddress').should(be.blank).type(users.student.current_address)
    browser.element('#permanentAddress').should(be.blank).type(users.student.current_address)

    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    browser.element('#submit').click()

    # THEN
    browser.element('#output #name').should(have.text(f'{users.student.first_name} {users.student.last_name}'))
    browser.element('#output #email').should(have.text(users.student.email))
    browser.element('#output #currentAddress').should(have.text(users.student.current_address))
    browser.element('#output #permanentAddress').should(have.text(users.student.current_address))
