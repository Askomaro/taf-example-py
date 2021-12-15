import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config.config import Config


class BasePageMixin:
    def __init__(self, driver: webdriver = None):
        self._page_name = self.__class__.__name__
        print(f'initialize {self._page_name}')

        self._driver = driver
        self._wait = WebDriverWait(self._driver, Config['explicit_wait_polling'])

    def get_url(self):
        return self._driver.current_url

    def _find_by(self, selector: str, by: By = By.XPATH) -> WebElement:
        el = self._wait.until(
            EC.presence_of_element_located((by, selector)),
            f'can not find {selector} on the page "{self._page_name}" page, '
            f'after {Config["explicit_wait_polling"]} second(s)')

        return el

    def _is_visible(self, selector: str, by: By = By.XPATH) -> WebElement:
        el = self._wait.until(
            EC.visibility_of_element_located((by, selector)),
            f'can not find {selector} on the page "{self._page_name}" page, '
            f'after {Config["explicit_wait_polling"]} second(s)')

        return el

    def _exists(self, selector: str, by: By = By.XPATH) -> bool:
        try:
            self._driver.find_element(by, selector)
        except NoSuchElementException:
            return False

        return True

    def _click_via_script_by(self, selector: str, by: By = By.XPATH):
        el = self._wait.until(EC.element_to_be_clickable((by, selector)),
                              f'element {selector} is not clickable on the page {self._page_name}')
        # hack to perform click using javascript
        self._driver.execute_script('arguments[0].click();', el)

    def _moveto_via_script_by(self, selector: str, by: By = By.XPATH, el: WebElement = None):
        if not el:
            el = self._find_by(selector, by)

        # hack
        self._driver.execute_script("arguments[0].scrollIntoView();", el)

    def _send_keys(self, selector: str, text: object, by: By = By.XPATH):
        txt = str(text)
        self._wait.until(EC.visibility_of_element_located((by, selector)), f'can not find {selector}')
        we = self._find_by(selector, by)

        we.clear()

        we.send_keys(txt)
        self._wait.until(EC.text_to_be_present_in_element_value((by, selector), txt),
                         f'text "{txt}" is not presented in {selector}')

    def _set_driver(self, driver: webdriver):
        self._driver = driver
        self._wait._driver = driver

    @staticmethod
    def _wait_conditions(predicate, timeout=None, period=0.25, *args, **kwargs):
        if not timeout:
            timeout = Config['explicit_wait_polling']

        end_time = time.time() + timeout
        while time.time() < end_time:
            if predicate(*args, **kwargs):
                return True
            time.sleep(period)
        return False
