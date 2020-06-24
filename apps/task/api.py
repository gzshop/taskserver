
from apps.base import BaseHandler
from utils.time_st import UtilTime
from utils.decorator.connector import Core_connector
from apps.task.task import order_handler

class Order(BaseHandler):

    @Core_connector(isTransaction=False,isTicket=False)
    async def post(self, *args, **kwargs):

        ut = UtilTime()

        runTime = ut.today.shift(seconds=int(self.application.settings.get("ordertime",1)))

        self.scheduler.add_job(order_handler, 'date',
                              run_date=runTime.datetime,
                              kwargs={
                                  "url":"{}/order/OrderCanleSys".format(self.application.settings.get("busiserver")),
                                  "data":{
                                      "orderid": self.data.get("orderid", None)
                                  }
                              })

        return None
