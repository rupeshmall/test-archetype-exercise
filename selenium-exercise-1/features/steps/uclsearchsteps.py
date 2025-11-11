import os
from behave import *
from selenium import webdriver
from utilities.TestDataHelper import ConfigReader, TestDataReader
from features.pages.uclsearchpo.searchpo import searchpo
from utilities.TestDataHelper.TestDataReader import Get_Env_Var
from features.pages import basepo
from features.common.customcontext import CustomContext

@given(u'I navigate to google')
def step_impl(context: CustomContext):
    url = Get_Env_Var(context, "googleurl")
    context.objsearchpo.navigate_to(url)

@given(u'I enter search string "{search_text}"')
def step_impl(context: CustomContext, search_text):
    context.objsearchpo.enter_text(search_text)

@when(u'I click on Search button')
def step_impl(context: CustomContext):
    context.objsearchpo.search_click()

@then(u'I should get the expected result "{expected_text}"')
def step_impl(context: CustomContext, expected_text):
    context.objsearchpo.text_check(expected_text)

@given(u'I enter search string from "{data_set}"')
def step_impl(context: CustomContext, data_set):
    search_text = TestDataReader.GetTestDataStringFromJsonFile(context.feature_name, data_set, "SearchData")
    context.objsearchpo.enter_text(search_text)

@then(u'I should get the expected result from "{data_set}"')
def step_impl(context: CustomContext, data_set):
    dataValues = TestDataReader.GetTestDataFromJsonFile(context.feature_name, data_set)
    context.objsearchpo.text_check_with_datavalues(dataValues)