from selenium.webdriver.common.by import By
from utilities.ReusableActions.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
import time


class loginpo(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Login with test account credentials
    txt_Username = (By.ID, "i0116")
    btn_Next = (By.ID, "idSIButton9")
    txt_Password = (By.ID, "i0118")

    #btn_Cookies = (By.ID, "bnp_btn_accept")

    def navigate_to(self, url):
        self.navigate_to_url(url)
        # try:
        #     self.accept_cookies()
        # except Exception as e:
        #     print("An exception occurred:", e)

    def enter_username_password(self, username, password):
        self.enter_text_on_element(self.txt_Username, username)
        self.click_on_element(self.btn_Next)
        self.enter_text_on_element(self.txt_Password, password)

    def click_signin(self):
        # signin button click
        self.click_on_element(self.btn_Next)
        # stay connected btn click
        self.click_on_element(self.btn_Next)

    # def accept_cookies(self):
    #     self.wait_for_element_with_waittime(self.btn_Cookies, 2)
    #     self.click_on_element(self.btn_Cookies)

    # def text_check(self, expected_text):
    #     actual_text = self.get_text_from_element(self.txt_Expected)
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
