
import json
from loguru import logger
from tasks.task_handler import order_handlers

def add_task(scheduler=None):

    scheduler.add_job(order_handlers, 'cron',
                      hour=3,
                      minute=0,
                      second=0)

if __name__ == '__main__':
    import sys,os
    from models.task import Cp
    PROJECT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir)
    if PROJECT_PATH not in sys.path:
        sys.path.insert(0, PROJECT_PATH)

    # import json
    #
    # from tasks.cp import CpTaskBase
    # from models.cp import Cp
    # from loguru import logger

    add_task()