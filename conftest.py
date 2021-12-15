import pytest
from selenium import webdriver

from config.config import Config


@pytest.fixture(scope='function')
def driver(request):
    print('initialize WebDriver')
    _driver = webdriver.Chrome()

    _driver.implicitly_wait(Config['implicitly_wait'])

    yield _driver

    if hasattr(request.node, 'report') and request.node.report:
        if request.node.report.failed:
            print('screenshot is saved')
            _driver.save_screenshot('test_results/screenshot.png')

    print('close WebDriver')
    _driver.quit()


# @pytest.fixture
# def user():
#     return PersonTypeEnum
