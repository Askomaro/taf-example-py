import pytest

from core.api.resources.films_resource import FilmsResource
from core.page_objects.main_page import MainPage


# @pytest.mark.skip(reason="no way of currently testing this")
def test__main_ui(driver):
    test_word_to_search = 'ZenHub'

    main_page = MainPage(driver)
    main_page\
        .open()\
        .search_and_go(test_word_to_search)\
        .open_first_result_page()

    assert driver.current_url == 'https://www.zenhub.com/'


def test__main_api():
    # arrange
    films_resource = FilmsResource()

    # act
    resp = films_resource.get_all_films()

    # assert
    assert resp['message'] == 'ok'
