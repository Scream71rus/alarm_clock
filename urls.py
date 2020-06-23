
from handlers.alarm_clock_handler import AlarmClockHandler
from handlers.ws_handler import WSHandler

urls = [
    (r'/api/v1/aclock?', AlarmClockHandler,),
    (r'/ws', WSHandler)
]