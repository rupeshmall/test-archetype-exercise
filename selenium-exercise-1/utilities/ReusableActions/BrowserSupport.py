from datetime import datetime
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.remote.remote_connection import RemoteConnection
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Load environment variables from .env file only if not already set
if not os.getenv("USE_LAMBDATEST"):
    load_dotenv()

def initializebrowser(browser_name, build_name, test_name):
    # Check environment variable to determine if running in GitHub Actions (LambdaTest) or locally
    use_lambdatest = os.getenv("USE_LAMBDATEST", "false").lower() == "true"

    if use_lambdatest:
        lt_username = os.getenv("LT_USERNAME")
        lt_access_key = os.getenv("LT_ACCESS_KEY")

        lt_grid_url = f"https://{lt_username}:{lt_access_key}@hub.lambdatest.com/wd/hub"

        capabilities = set_lambdatest_capabilities(browser_name, lt_username, lt_access_key, build_name, test_name)

        # Set Chrome options and add them to the desired capabilities
        if browser_name.upper().startswith("CHROME"):
            options = setchromeoptions(browser_name)
            for key, value in capabilities.items():
                options.set_capability(key, value)

        executor = RemoteConnection(lt_grid_url)

        driver = webdriver.Remote(
            command_executor=executor,
            options=options
        )
        print("Browser initialised via lambda test")
    else:
        # Local browser initialization
        match browser_name.upper():
            case "CHROME" | "CHROME-HEADLESS" | "CHROME-INCOGNITO" | "CHROME-PROFILE":
                #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=setchromeoptions(browser_name))
                driver = webdriver.Chrome(options=setchromeoptions(browser_name))
            case "FIREFOX" | "FIREFOX-PRIVATE" | "FIREFOX-PROFILE":
                driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            case "EDGE":
                driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
            case _:
                driver = None
        print("---> Browser initialised via local route")

    if driver:
        driver.implicitly_wait(30)
        driver.maximize_window()
        print("---> Browser initialised successfully")
    else:
        print("---> Failed to initialise")

    return driver

def setchromeoptions(browser_name):
    options = ChromeOptions()
    options.set_capability("acceptInsecureCerts", True)
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("prefs", {
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True  # This option ensures PDFs are opened automatically
    })
    if browser_name.upper() == "CHROME-HEADLESS":
        options.add_argument("--headless")
    if browser_name.upper() == "CHROME-INCOGNITO":
        options.add_argument("--incognito")
        prefs = {"profile.default_content_settings.popups": 0}
        options.add_experimental_option("prefs", prefs)
    return options

def set_lambdatest_capabilities(browser_name, lt_username, lt_access_key, build_name, test_name):
    # build_name = f"Python_Selenium_Archetype-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
    run_in_on_premise = os.getenv("RUN_IN_ON_PREMISE", "false").lower() == "true"
    capabilities = {
        "build": build_name,  # You can provide a build name here
        "name": test_name,    # You can provide a test name here
        "platform": "Windows 10",    # Example platform, can be changed
        "browserName": browser_name,     # Example browser, should be set based on `browser_name`
        "version": "latest",         # Browser version, 'latest' for the most recent version
        "resolution": "1280x1024",   # Example resolution, can be changed
        "selenium_version": "4.0.0", # Selenium version
        "acceptInsecureCerts": True,
        "video": True,
        "console": True,
        "network": True,               # Enable network logs
        "network.har": True
    }

    if run_in_on_premise:
        # Include tunnel-related details for on-premise setup
        capabilities.update({
            "user": lt_username, 
            "accessKey": lt_access_key,
            "tunnel": True,  
            "tunnelName": "Test_Tunnel_Name",  # Name of the tunnel
        })
    else:
        capabilities.update({
            "user": lt_username, 
            "accessKey": lt_access_key,
            "tunnel": False,  
            "tunnelName": "Test_Tunnel_Name",  # Name of the 
            "geoLocation": "GB"
        })

    if browser_name.upper() == "CHROME-HEADLESS":
        capabilities["browserName"] = "Chrome"
        capabilities["goog:chromeOptions"] = {"args": ["--headless", "--disable-gpu"]}
    elif browser_name.upper() == "FIREFOX":
        capabilities["browserName"] = "Firefox"
    elif browser_name.upper() == "EDGE":
        capabilities["browserName"] = "MicrosoftEdge"

    return capabilities
