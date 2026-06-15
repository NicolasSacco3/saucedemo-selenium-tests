from pages.login_page import Login_Page


def test_login( driver ):
    login_page = Login_Page(driver)
    login_page.open()
