
import json

from cerberus import Validator
import tornado.web

from utils import ObjectEncoder


class BaseHandler(tornado.web.RequestHandler):

    @property
    def request_data(self):
        if not hasattr(self, "_request_data"):
            self._request_data = json.loads(self.request.body.decode()) \
                if self.request.body else {}

            self._request_data = dict(filter(lambda i: i[1] != '', self._request_data.items()))

        return self._request_data

    def response(self, data):
        self.set_header('Content-Type', 'application/json')
        data = json.dumps(data, cls=ObjectEncoder)
        self.finish(data)

    def validator(self, schema=None, data=None):
        if schema and data:
            v = Validator()
            v.schema = schema
            v.validate(data)

            return data, v.errors
        else:
            return data, True
