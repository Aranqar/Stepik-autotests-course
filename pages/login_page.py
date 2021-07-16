from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.url, "Not found login_url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_all_registration_fields(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email field is not " \
                                                                               "presented "
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Registration password field is not" \
                                                                                  " presented "
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASS_AGAIN), "Registration pass again is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_field2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_AGAIN)
        password_field1.send_keys(password)
        password_field2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()
