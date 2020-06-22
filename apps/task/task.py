


from models.task import Order
from loguru import logger

def order_handler(**kwargs):

    db = kwargs.get("db")
    orderid = kwargs.get("orderid")

    logger.info("订单号{}".format(orderid))
    with db.atomic():
        orders = Order.select().where(Order.orderid == orderid).for_update()
        for order in orders:
            if order.status == '0':
                order.status ='9'
                order.save()

                logger.info("订单号{}处理成功!".format(orderid))

