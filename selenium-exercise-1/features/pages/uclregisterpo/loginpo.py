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
        