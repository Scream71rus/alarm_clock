
from models.base_model import BaseModel


CREATE_SCHEMA = {
    'message': {'type': 'string', 'minlength': 2},
    'timer': {'type': 'datetime'}
}


class AlertClockModel(BaseModel):

    @classmethod
    async def get_list(cls):
        sql = "select * from alert_clock.clock order by timer"
        cursor = await cls.db.fetch(sql)
        return cursor

    @classmethod
    async def get_list_by_time_interval(cls, time_from, time_to):
        sql = "select * from alert_clock.clock where timer >= $1 and timer <= $2 order by timer"
        cursor = await cls.db.fetch(sql, time_from, time_to)
        return cursor

    @classmethod
    async def create(cls, data):
        sql = "insert into alert_clock.clock(message, timer) values($1, $2) returning id"
        cursor = await cls.db.fetchval(sql, data.get('message'), data.get('timer'))
        data['id'] = cursor
        return data

    @classmethod
    async def delete_by_id(cls, alert_clock_id):
        sql = "delete from alert_clock.clock where id = $1"
        await cls.db.fetch(sql, alert_clock_id)
