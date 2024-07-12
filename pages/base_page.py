from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self):
        return self.driver.title

    def get_text(self, by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).text

    def take_screenshot(self, image_name):
        self.driver.save_screenshot(f"../screenshot/{image_name}.png")

    def is_display(self, by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def scroll_down(self,froms,to):
        self.driver.execute_script(f"window.scrollBy({froms},{to})")