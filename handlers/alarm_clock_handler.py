
import datetime

from handlers.base_handler import BaseHandler
from models.alert_clock_model import AlertClockModel
from models.alert_clock_model import CREATE_SCHEMA


class AlarmClockHandler(BaseHandler):

    async def get(self):
        alert_clock_list = await AlertClockModel.get_list()
        self.response(alert_clock_list)

    async def post(self):
        data = {
            'message': self.request_data.get('message'),
            'timer': datetime.datetime.strptime(self.request_data.get('timer'), "%Y-%m-%d %H:%M"),
        }

        data, errors = self.validator(schema=CREATE_SCHEMA, data=data)
        if not errors:
            data = await AlertClockModel.create(data)

            self.response({
                'ok': True,
                'data': data
            })

        else:
            self.response({
                'ok': False,
                'errors': errors
            })
