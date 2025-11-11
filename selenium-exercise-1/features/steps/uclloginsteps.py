import os
from behave import *
from selenium import webdriver
from utilities.TestDataHelper import ConfigReader, TestDataReader
from features.pages.uclsearchpo.searchpo import searchpo
from utilities.TestDataHelper.TestDataReader import Get_Env_Var
from features.pages import basepo
from features.common.customcontext import CustomContext


@given(u"I navigate to the UCL cubase app portal")
def step_impl(context: CustomContext):
    url = Get_Env_Var(context, "cubaseurl")
    context.objloginpo.navigate_to(url)


@given(u"Microsoft login page is displayed")
def step_impl(context: CustomContext):
    expected_title = TestDataReader.GetTestDataStringFromJsonFile(
        context.feature_name, "Loginpage", "Title"
    )
    context.objloginpo.verify_title(expected_title)


@when(u"I enter a valid Microsoft test account username and password")
def step_impl(context: CustomContext):
    username = Get_Env_Var(context, "testemail")
    password = os.getenv("TESTPASSWORD")
    context.objloginpo.enter_username_password(username, password)


@when(u"I click on the Sign in button")
def step_impl(context: CustomContext):
    context.objloginpo.click_signin()


@then(u"I should be redirected to the application home page")
def step_impl(context: CustomContext):
    expected_txt_h1 = TestDataReader.GetTestDataStringFromJsonFile(
        context.feature_name, "Portalpage", "H2"
    )
    context.objregisterpo.text_check(expected_txt_h1)
