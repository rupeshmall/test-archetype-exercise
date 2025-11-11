from features.common.customcontext import CustomContext
from features.pages.uclsearchpo.searchpo import searchpo
from features.pages.uclregisterpo.registerpo import registerpo
from features.pages.uclregisterpo.loginpo import loginpo


# Initialise the pages to test
def initialise_pages(context: CustomContext):
    context.objsearchpo = searchpo(context.driver)
    context.objloginpo = loginpo(context.driver)
    context.objregisterpo = registerpo(context.driver)
