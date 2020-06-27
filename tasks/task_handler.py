
from requests import request
from loguru import logger
from config import config_insert

def order_handlers():

    response = request(
        method="POST",
        url="{}/order/OrderCanleSysEx".format(config_insert['common'].get("busiserver")),
        json={"data":{}})

    logger.info(response.text)
    logger.info("晚间批量处理!")
