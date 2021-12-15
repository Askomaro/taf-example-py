from selenium import webdriver


def get():
    print('initiate chrome webdriver')

    _driver = webdriver.Chrome()
    yield _driver

    print('close chrome webdriver')
    _driver.quit()
