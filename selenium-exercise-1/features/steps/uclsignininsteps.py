import os
from behave import *
from utilities.TestDataHelper import ConfigReader, TestDataReader
from utilities.TestDataHelper.TestDataReader import Get_Env_Var
from features.common.customcontext import CustomContext


@given(u"the user navigates to the application URL")
def step_impl(context: CustomContext):
    url = Get_Env_Var(context, "portalurl")
    context.objsigninpo.navigate_to_url(url)


@given(u"the Microsoft login page is displayed")
def step_impl(context: CustomContext):
    expected_title = TestDataReader.GetTestDataStringFromJsonFile(
        context.feature_name, "Loginpage", "Title"
    )
    context.objsigninpo.verify_title(expected_title)


@when(u"the user enters a valid Microsoft test account username and password")
def step_impl(context: CustomContext):
    username = Get_Env_Var(context, "testemail")
    password = os.getenv("TESTPASSWORD")
    context.objsigninpo.enter_test_username_password(username, password)


@when(u"clicks on the Sign in button")
def step_impl(context: CustomContext):
    context.objsigninpo.click_testuser_signin()


@then(u"the user should be redirected to the application home page")
def step_impl(context: CustomContext):
    expected_txt_h1 = TestDataReader.GetTestDataStringFromJsonFile(context.feature_name, "Portalpage", "H1")
    context.objsigninpo.verify_portal_heading(expected_txt_h1)


@given(u'the applicant clicks on the Sign in button')
def step_impl(context: CustomContext):
    context.objsigninpo.click_portal_signin_btn()


@given(u'the applicant is navigated to the applicant Sign in screen')
def step_impl(context: CustomContext):
    expected_txt_h2 = TestDataReader.GetTestDataStringFromJsonFile(context.feature_name, "Signuppage", "H2")
    context.objsigninpo.verify_signup_heading(expected_txt_h2)


@when(u'the applicant clicks on the Sign up now link')
def step_impl(context: CustomContext):
    context.objsigninpo.click_signup_btn()


@when(u'enters the valid user details {data_set}')
def step_impl(context: CustomContext, data_set):
    data_values = TestDataReader.GetTestDataFromJsonFile(context.feature_name, data_set)
    context.objsigninpo.enter_user_details(data_values)


@when(u'clicks on Create button')
def step_impl(context: CustomContext):
    context.objsigninpo.click_create_account_btn()


@then(u'the applicant should be redirected to the application home page and successfully signed in {data_set}')
def step_impl(context: CustomContext, data_set):
    message = TestDataReader.GetTestDataStringFromJsonFile(context.feature_name, "Portalpage", "LoginSuccessH1")
    data_values = TestDataReader.GetTestDataFromJsonFile(context.feature_name, data_set)
    expected_txt_h1 = message + ', ' +  data_values["GivenName"]
    context.objsigninpo.verify_portal_heading(expected_txt_h1)
