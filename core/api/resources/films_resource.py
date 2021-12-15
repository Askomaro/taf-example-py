from core.api.resources.base_resource import BaseResource


class FilmsResource(BaseResource):
    _URL_API_PATH = '/planets/1'

    def __init__(self):
        BaseResource.__init__(self)
        self.__url_path = '%s%s%s' % (self._SCHEMA,
                                      self._HOST,
                                      self._URL_API_PATH)

    def get_all_films(self):
        return self._get_response(self.__url_path)

    def get_film(self, film_id):
        return self._get_response('%s/%s' % (self.__url_path, film_id))
