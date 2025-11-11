from selenium.webdriver.common.by import By
from utilities.ReusableActions.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time


class registerpo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Portal page
    expected_txt_h1 = (By.CLASS_NAME, "user-welcome")
    btn_Signin = (By.XPATH, "//a[contains(@title, 'Sign in')]")

    # Signin page
    btn_Create_account = (By.ID, "createAccount")

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
    # btn_Cookies = (By.ID, "bnp_btn_accept")

    def navigate_to(self, url):
        self.navigate_to_url(url)
        try:
            self.accept_cookies()
        except Exception as e:
            print("An exception occurred:", e)

    def enter_text(self, search_text):
        self.enter_text_on_element(self.txt_Search, search_text)

    def search_click(self):
        self.click_via_javascript(self.btn_Search)

    def accept_cookies(self):
        self.wait_for_element_with_waittime(self.btn_Cookies, 2)
        self.click_on_element(self.btn_Cookies)

    def text_check(self, expected_text):
        actual_text = self.get_text_from_element(self.expected_txt_h1)
        assert (
            expected_text in actual_text
        ), f"Expected to find '{expected_text}' in '{actual_text}'"

        # assert actual_text == expected_text, f"Expected: {expected_text}, Actual: {actual_text}"
        # assert actual_text.__eq__(expected_text)

    def text_check_with_datavalues(self, data_values):
        actual_text = self.get_text_from_element(self.txt_Expected)
        expected_text = data_values.get("ExpectedResult")
        assert (
            expected_text in actual_text
        ), f"Expected to find '{expected_text}' in '{actual_text}'"
