from features.common.customcontext import CustomContext
from features.pages.uclsearchpo.searchpo import searchpo


# Initialise the pages to test
def initialise_pages(context: CustomContext):
    context.objsearchpo = searchpo(context.driver)
