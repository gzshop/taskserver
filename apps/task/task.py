


from models.task import Order

def order_handler(**kwargs):

    db = kwargs.get("db")
    orderid = kwargs.get("orderid")

    with db.atomic():
        orders = Order.select().where(Order.orderid == orderid).for_update()
        for order in orders:
            if order.status == '0':
                order.status ='9'
                order.save()

