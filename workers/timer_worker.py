
import datetime

from tornado.gen import sleep

from models.alert_clock_model import AlertClockModel
from handlers.ws_handler import WSHandler


class TimerWorker:
    @property
    def application(self):
        return self._application

    def __init__(self, application=None):
        self._application = application

    async def run(self):
        while True:
            await sleep(.5)

            time_from = datetime.datetime.now()
            time_to = time_from + datetime.timedelta(minutes=2)

            alert_clock_list = await AlertClockModel.get_list_by_time_interval(time_from, time_to)

            for alert_clock in alert_clock_list:
                time_now = datetime.datetime.now().timestamp()

                await sleep(int((alert_clock.get('timer').timestamp() - time_now)))

                for ws_user in WSHandler.ws_users:
                    ws_user.write_message(alert_clock.get('message'))

                await AlertClockModel.delete_by_id(alert_clock.get('id'))
