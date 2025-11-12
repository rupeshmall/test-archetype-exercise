from selenium.webdriver.common.by import By
from utilities.ReusableActions.BasePage import BasePage


class signinpo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Login with test account credentials
    txt_test_username = (By.ID, "i0116")
    btn_test_login = (By.ID, "idSIButton9")
    txt_test_password = (By.ID, "i0118")

     # Portal page
    expected_txt_portal_h1 = (By.CLASS_NAME, "user-welcome")
    btn_portal_cookies = (By.NAME, "cookies")
    btn_portal_signin = (By.XPATH, "//a[@title='Sign in' and @role='menuitem']")

    # Signup page
    expected_txt_signup = (By.XPATH, "//div[contains(@class, 'intro')]/h2")
    btn_signup = (By.ID, "createAccount")

    # Create account page
    txt_create_email = (By.ID, "email")
    txt_create_password = (By.ID, "newPassword")
    txt_create_confirm_password = (By.ID, "reenterPassword")
    txt_create_name = (By.ID, "givenName")
    txt_create_surname = (By.ID, "surname")
    btn_create_account = (By.ID, "continue")
    # txt_Expected = (By.XPATH,"(//ol[contains(@id,'results')]//h2)[1]")

    def navigate_to(self, url):
        self.navigate_to_url(url)


    def enter_test_username_password(self, username, password):
        self.enter_text_on_element(self.txt_test_username, username)
        self.click_on_element(self.btn_test_login)
        self.enter_text_on_element(self.txt_test_password, password)


    def click_testuser_signin(self):
        # signin button click
        self.click_on_element(self.btn_test_login)
        # stay connected btn click
        self.click_on_element(self.btn_test_login)
    

    def verify_portal_heading(self, expected_text):
        actual_text = self.get_text_from_element(self.expected_txt_portal_h1)
        assert (expected_text in actual_text), f"Expected to find '{expected_text}' in '{actual_text}'"


    def click_portal_signin_btn(self):
        self.click_on_element(self.btn_portal_cookies)
        self.click_on_element(self.btn_portal_signin)        


    def verify_signup_heading(self, expected_text):
        actual_text = self.get_text_from_element(self.expected_txt_signup)
        print(actual_text)
        assert (expected_text in actual_text), f"Expected to find '{expected_text}' in '{actual_text}'"


    def click_signup_btn(self):
        self.click_on_element(self.btn_signup)


    def enter_user_details(self, data_values):
        self.enter_text_on_element(self.txt_create_email, data_values["EmailAddress"])
        self.enter_text_on_element(self.txt_create_password, data_values["Password"])
        self.enter_text_on_element(self.txt_create_confirm_password, data_values["ConfirmPassword"])
        self.enter_text_on_element(self.txt_create_name, data_values["GivenName"])
        self.enter_text_on_element(self.txt_create_surname, data_values["Surname"])


    def click_create_account_btn(self):
        self.click_on_element(self.btn_create_account)
