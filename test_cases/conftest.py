import  pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--env", action="store", default='prod')

@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    env = request.config.getoption("--env")

#envoirnments
    if env == "dev":
        base_url = "https://dev.pharmeasy.in/"
    elif env == "staging":
        base_url = "https://staging.pharmeasy.in/"
    elif env == "prod":
        base_url = "https://pharmeasy.in/"
    else:
        base_url = "https://pharmeasy.in/"

#browser
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()

    driver.get(base_url)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
    print("done")
