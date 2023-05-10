from wrm_selene_python_hw_10.application import app
from wrm_selene_python_hw_10.data import users


def test_text_box(browser_control):
    # GIVEN
    app.open()
    app.menu_panel.open_panel_menu_item(link_text='Text Box')

    # WHEN
    app.text_box.register(users.student)

    # THEN
    app.text_box.should_have_data(users.student)
