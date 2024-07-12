import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

def pytest_addoption(parser):
    # Add command-line options for browser name and environment
    parser.addoption("--browser_name", action="store", default="chrome", help="Name of the browser to use (e.g., chrome, firefox, edge)")
    parser.addoption("--env", action="store", default='prod', help="Environment to test against (e.g., dev, staging, prod)")

@pytest.fixture(scope="function")
def setup(request):
    # Retrieve command-line options for browser name and environment
    browser_name = request.config.getoption("--browser_name")
    env = request.config.getoption("--env")

    # Set the base URL based on the environment
    if env == "dev":
        base_url = "https://dev.pharmeasy.in/"
    elif env == "staging":
        base_url = "https://staging.pharmeasy.in/"
    elif env == "prod":
        base_url = "https://pharmeasy.in/"
    else:
        base_url = "https://pharmeasy.in/"

    # Configure browser options
    option = Options()
    option.add_argument("--headless")  # Run Chrome in headless mode
    optionsfire = Options()
    optionsfire.add_argument("--headless")  # Run Firefox in headless mode

    # Initialize the WebDriver based on the browser name
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=option)
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(options=optionsfire)
    else:
        driver = webdriver.Chrome()  # Default to Chrome if an unknown browser is specified

    # Open the base URL and configure WebDriver settings
    driver.get(base_url)
    driver.implicitly_wait(10)  # Set implicit wait time
    driver.maximize_window()  # Maximize the browser window

    # Attach the WebDriver instance to the test class
    request.cls.driver = driver

    # Teardown: Quit the WebDriver instance after the test completes
    yield driver
    driver.quit()
