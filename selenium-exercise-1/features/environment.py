from datetime import datetime
import os
import allure
from allure_commons.types import AttachmentType
from features.pages import basepo
from features.common.customcontext import CustomContext
from utilities.ReusableActions import BrowserSupport
from utilities.TestDataHelper.ConfigReader import config_reader
from utilities.TestDataHelper.TestDataReader import Get_Env_Var


def before_all(context: CustomContext):
    context.build_name = (
        f"Python_Selenium_Archetype-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    )
   

def before_scenario(context: CustomContext, scenario):
    context.feature_name = context.feature.name
    context.test_name = scenario.name
    yaml_config = config_reader.load_config("configurations/config.yaml")
    context.behave_config = config_reader.derive_config(context.config, yaml_config)
    context.driver = BrowserSupport.initializebrowser(
        Get_Env_Var(context, "browser_param", "browser"),
        context.build_name,
        context.test_name,
    )
    context.feature_name = context.scenario.feature.name
    basepo.initialise_pages(context)
    print("---> Initilised pages succesfully")


def after_scenario(context: CustomContext, scenario):
    context.driver.quit()
    print("Failure Reason:", context.failure_reason)


def after_step(context: CustomContext, step):
    context.failure_reason = step.exception
    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="failed_screenshot",
            attachment_type=AttachmentType.PNG,
        )
