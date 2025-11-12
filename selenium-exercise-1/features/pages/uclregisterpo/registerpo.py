from selenium.webdriver.common.by import By
from utilities.ReusableActions.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time


class registerpo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Portal page
    expected_txt_h1 = (By.CLASS_NAME, "user-welcome")
    btn_Cookies = (By.NAME, "cookies")
    btn_Signin = (By.XPATH, "//a[contains(@title, 'Sign in')]")

    # Signup page
    expected_signup_txt = (By.XPATH, "//div[contains(@class, 'intro')/h2]")
    btn_signup = (By.ID, "createAccount")

    # Create account page
    txt_new_email = (By.ID, "email")
    txt_new_password = (By.ID, "newPassword")
    txt_confirm_password = (By.ID, "reenterPassword")
    txt_given_name = (By.ID, "givenName")
    txt_surname = (By.ID, "surname")
    btn_create_account = (By.ID, "continue")

    # txt_Search = (By.NAME, "q")
    # btn_Search = (By.NAME, "search")
    # txt_Expected = (By.XPATH,"(//ol[contains(@id,'results')]//h2)[1]")
    # txt_Expected = (By.XPATH, "(//a[contains(text(),'UCL -')])[1]")

    def navigate_to(self, url):
        self.navigate_to_url(url)
        try:
            self.accept_cookies()
        except Exception as e:
            print("An exception occurred:", e)

    def click_signin_btn(self):
        self.click_on_element(self.btn_Signin)        

    def verify_cubasepage_heading(self, expected_text):
        actual_text = self.get_text_from_element(self.expected_txt_h1)
        assert (
            expected_text in actual_text
        ), f"Expected to find '{expected_text}' in '{actual_text}'"


    def verify_signinpage_heading(self, expected_text):
        actual_text = self.get_text_from_element(self.expected_signup_txt)
        assert (
            expected_text in actual_text
        ), f"Expected to find '{expected_text}' in '{actual_text}'"


    def click_signup_btn(self):
        self.click_on_element(self.btn_signup)
    
    def enter_user_details(self, data_values):
        self.enter_text_on_element(data_values.get("EmailAddress"))
        self.enter_text_on_element(data_values.get("Password"))
        self.enter_text_on_element(data_values.get("GivenName"))
        self.enter_text_on_element(data_values.get("Surname"))


    def click_create_account_btn(self):
        self.click_on_element(self.btn_create_account)

    # def enter_text(self, search_text):
    #     self.enter_text_on_element(self.txt_Search, search_text)

    # def search_click(self):
    #     self.click_via_javascript(self.btn_Search)

    # def accept_cookies(self):
    #     self.wait_for_element_with_waittime(self.btn_Cookies, 2)
    #     self.click_on_element(self.btn_Cookies)

    # def text_check(self, expected_text):
    #     actual_text = self.get_text_from_element(expected_text)
    #     assert (
    #         expected_text in actual_text
    #     ), f"Expected to find '{expected_text}' in '{actual_text}'"

    #     # assert actual_text == expected_text, f"Expected: {expected_text}, Actual: {actual_text}"
    #     # assert actual_text.__eq__(expected_text)

    # def text_check_with_datavalues(self, data_values):
    #     actual_text = self.get_text_from_element(self.txt_Expected)
    #     expected_text = data_values.get("ExpectedResult")
    #     assert (
    #         expected_text in actual_text
    #     ), f"Expected to find '{expected_text}' in '{actual_text}'"
