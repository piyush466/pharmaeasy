from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basepage:

    def __init__(self, driver):
        # Initialize the page object with the WebDriver instance
        self.driver = driver

    def do_click(self, by_locator):
        # Wait until the element located by `by_locator` is visible and then perform a click action
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        # Wait until the element located by `by_locator` is visible and then send `text` to it
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self):
        # Return the current page title
        return self.driver.title

    def get_text(self, by_locator):
        # Wait until the element located by `by_locator` is visible and return its text content
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text

    def take_screenshot(self, image_name):
        # Capture a screenshot and save it with the specified `image_name`
        self.driver.save_screenshot(f"../screenshot/{image_name}.png")

    def is_display(self, by_locator):
        # Wait until the element located by `by_locator` is visible and return whether it is displayed
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def scroll_down(self, froms, to):
        # Scroll the page window by the specified amount (`froms` and `to`)
        self.driver.execute_script(f"window.scrollBy({froms},{to})")
