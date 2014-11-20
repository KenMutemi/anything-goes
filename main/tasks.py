from celery.decorators import periodic_task
from celery.task.schedules import crontab
from main.utils.summary_update import update_summaries
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@periodic_task(run_every=(crontab(hour=10, minute=22, day_of_week="*")))
def summary_updater():
    logger.info("Start task")
    update_summaries()
