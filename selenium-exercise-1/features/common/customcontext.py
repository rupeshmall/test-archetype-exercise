from selenium.webdriver.remote.webdriver import WebDriver
from behave.runner import Context
from typing import TYPE_CHECKING, Optional
from features.pages.uclsearchpo.searchpo import searchpo
from features.pages.uclregisterpo.registerpo import registerpo
from features.pages.uclregisterpo.loginpo import loginpo


class CustomContext(Context):
    # Archetype specific context objects gets declared here
    driver: WebDriver
    feature_name: Optional[str] = None
    behave_config = None
    build_name: Optional[str] = None
    test_name: Optional[str] = None

    # All the Page objects to be created in basepo gets declared here
    objsearchpo: "searchpo"
    objloginpo: "loginpo"
    objregisterpo: "registerpo"

    # All the context variables to be used in the project gets declared here
    myoutoutid = None
