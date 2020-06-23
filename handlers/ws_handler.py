
from tornado.websocket import WebSocketHandler


class WSHandler(WebSocketHandler):

    ws_users = set()

    def check_origin(self, origin):
        return True

    def open(self):
        self.ws_users.add(self)

    def on_close(self):
        self.ws_users.remove(self)

