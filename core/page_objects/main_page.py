from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from config.config import Config
from core.helpers import webdriver_provider
from core.page_objects.base_page_mixin import BasePageMixin


class MainPage(BasePageMixin):
    # XPATH locators
    __SEARCH_INPUT_LOCATOR = 'input.gLFyf'
    __FIRST_SEARCH_RESULT_LOCATOR = 'h3.LC20lb'
    __SEARCH_BUTTON_LOCATOR = '//input[@class="gNO89b"]'

    # '//a[@class="button log-in"][contains(text(), "Увійти")]'
    # '//input[@id="eLogin"]'
    # "//h3[contains(text(),'Resources')]/following-sibling::div/a[contains(text(), 'Blog')]"

    def __init__(self, driver=None):
        super(MainPage, self) \
            .__init__(next(webdriver_provider.get()) if not driver else driver)
        self.__START_PAGE_URL = Config['base_url']

    def open(self):
        print(f'open base url: {self.__START_PAGE_URL}')
        self._driver.get(self.__START_PAGE_URL)

        return self

    def search_and_go(self, text: str):
        self._send_keys(self.__SEARCH_INPUT_LOCATOR, text, By.CSS_SELECTOR)
        self._find_by(self.__SEARCH_BUTTON_LOCATOR).click()

        return self

    def open_first_result_page(self):
        self._find_by(self.__FIRST_SEARCH_RESULT_LOCATOR, By.CSS_SELECTOR)\
            .click()

        return self

    def _wait_auction_page_load(self):
        print('wait auction page loaded')
        if not self._exists(self.__AUCTION_PAGE_MARK):
            print('failed to load page')
            raise NoSuchElementException(
                'can not load auction page by webelement: {}'.format(self.__AUCTION_PAGE_MARK))
