
from requests import request
from loguru import logger

def order_handler(**kwargs):


    response = request(method="POST",url=kwargs.get('url'),json=kwargs.get("data"))

    logger.info(response.text)

