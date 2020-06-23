


from models.task import Order
from loguru import logger
from utils.database.mysql import MysqlPool

async def order_handler(**kwargs):

    db = kwargs.get("db")
    orderid = kwargs.get("orderid")

    # db = MysqlPoolSync().get_conn
    # db.ping(reconnect=True)

    logger.info("订单号{}".format(orderid))
    async with MysqlPool().get_conn.atomic_async():
        res = await db.execute(Order.select().where(Order.orderid == orderid).for_update())

        for order in res:
            if order.status == '0':
                order.status ='9'
                await db.update(order)

                logger.info("订单号{}处理成功!".format(orderid))

