from celery.utils.log import get_task_logger
from celery import shared_task



@shared_task
def save_tickets(view, data, *args, **kwargs):
    return super(view).create(data, *args, **kwargs)

#
# logger = get_task_logger(__name__)
#
# logger.info("Saved new ticket")
