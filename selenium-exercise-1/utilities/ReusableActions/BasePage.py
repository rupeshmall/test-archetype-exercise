from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import string

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def verify_title(self, page_title):
        assert self.driver.title == page_title, f"Expected: {page_title}, Actual: {self.driver.title}"

    def verify_title_contains(self, page_title):
        assert page_title in self.driver.title, f"Expected: {self.driver.title}, Actual: {page_title}"

    def click_on_element(self, element_locator):
        try:
            self.wait_for_element_with_waittime(EC.element_to_be_clickable(element_locator),10)
            self.driver.find_element(*element_locator).click()
        except Exception as e:
            self.click_via_javascript(element_locator)

    def click_via_javascript(self, element_locator):
        js = "arguments[0].click();"
        self.driver.execute_script(js, self.driver.find_element(*element_locator))

    def enter_text_on_element(self, element_locator, text_to_enter):
        status = self.wait_for_element_with_waittime(EC.element_to_be_clickable(element_locator),10)
        self.driver.find_element(*element_locator).send_keys(text_to_enter)
    
    def find_locator_element(self, element_locator):
        return self.driver.find_element(*element_locator)

    def get_text_from_element(self, element_locator):
        return self.driver.find_element(*element_locator).text
    
    def enter_text_and_click_enter(self, element_locator, text_to_enter):
        self.click_on_element(element_locator)
        self.enter_text_on_element(element_locator, text_to_enter)
        self.enter_text_on_element(element_locator, Keys.ENTER)

    def click_and_enter_text_on_element(self, element_locator, text_to_enter):
        self.click_on_element(element_locator)
        self.enter_text_on_element(element_locator, text_to_enter)

    def clear_and_enter_text_on_element(self, element_locator, text_to_enter ):
        self.clear_element(element_locator)
        self.enter_text_on_element(element_locator, text_to_enter)

    def clear_element(self, element_locator):
        self.driver.find_element(*element_locator).clear()
    
    def select_dropdown_element(self, element_locator, text_to_select):
        dropdown = Select(self.driver.find_element(*element_locator))
        dropdown.select_by_visible_text(text_to_select)

    def select_dropdown_element_by_value(self, element_locator, value_to_select):
        dropdown = Select(self.driver.find_element(*element_locator))
        dropdown.select_by_value(value_to_select)

    def select_dropdown_random_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        select = Select(element)
        available_opts = []
        """ Exclude the empty option from the available options """
        for opts in select.options:
            if opts.get_attribute("value") != "":
                available_opts.append(opts)

        """ Randomly select an option from the available options """
        selected_opt = random.choice(available_opts)
        val_selected = selected_opt.get_attribute("value")

        """ If the randomly selected option is empty, select a different option """
        if val_selected == "":
            selected_opt = random.choice(available_opts)
            val_selected = selected_opt.get_attribute("value")

        """ Select the chosen option in the dropdown """
        self.SelectTextFromDropdown(element_locator, value=val_selected)
        return val_selected

    def select_checkbox_element(self, element_locator):
        checkbox = self.driver.find_element(*element_locator)
        if checkbox.is_selected():
            self.click_on_element(element_locator)
    
    def switch_to_iframe(self, element_locator):
        frame = self.FindElement(element_locator)
        self.driver.switch_to.frame(frame)

    def switch_back_from_iframe(self):
        self.driver.switch_to.default_content()

    def scroll_to(self, x_position=0, y_position=0):
        js = f"window.scrollTo({x_position}, {y_position});"
        self.driver.execute_script(js)

    def scroll_to_element(self, element_locator):
        self.sleep(1)
        js = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js, self.driver.find_element(*element_locator))

    def zoomin_and_zoomout(self, zoom_percentage):
        js = "document.body.style.zoom='"+ zoom_percentage + "%'"
        self.driver.execute_script(js)

    def implicit_wait(self, wait_time):
        self.driver.implicitly_wait(wait_time)

    def get_element(self, element_locator):
        try:
            return self.driver.find_element(*element_locator) 
        except Exception as e:
            return 0
        
    def find_element(self, element_locator):
        element = self.driver.find_element(*element_locator)
        return element

    def find_elements(self, element_locator):
        elements = self.driver.find_elements(*element_locator)
        return elements
    
    def wait_for_element(self, condition):
        self.implicit_wait(10)
        try:
            element = WebDriverWait(self.driver, 10).until(condition)
            self.implicit_wait(30)
            return True                                         
        except Exception as e:
            self.implicit_wait(30)
            return False
        
    def wait_for_element_with_waittime(self, condition, wait_time):
        self.implicit_wait(wait_time)
        try:
            element = WebDriverWait(self.driver, wait_time).until(condition)
            self.implicit_wait(30)
            return True                                         
        except Exception as e:
            print(e)
            self.implicit_wait(30)
            return False
        
    def wait_for_network_idle(self, wait_time):
        i = 0
        while i < 5:
            wait = WebDriverWait(self.driver, wait_time)
            # wait.until(lambda Driver: (self.driver.execute_script("return (window.jQuery != null) ? jQuery.active === 0 : true")))
            self.driver.execute_script("return (window.jQuery != null) ? jQuery.active === 0 : true")
            if i > 0:
                time.sleep(3)
            i += 1
            if "Loading" not in self.driver.title:
                break

    def sleep(self, wait_time):
        time.sleep(wait_time)

    def get_shadow_root(self, shadow_host, selectors):
        root = None
        for selector in selectors:
            root = self.driver.execute_script(
                "return arguments[0].shadowRoot.querySelector(arguments[1])", shadow_host, selector)
        return root
    
    def verify_and_throw_error(self, actual, expected):
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    def switch_tab_by_title(self, desired_title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == desired_title:
                print(f"Switched to tab: {self.driver.title}")
                break

    def close_tab_by_title(self, desired_title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == desired_title:
                self.driver.close()
                break

    def generate_random_string(self, length):
        characters = string.ascii_letters  
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string
    
    def generate_random_number(self, length):
        characters = string.digits  
        random_number = ''.join(random.choice(characters) for _ in range(length))
        return random_number