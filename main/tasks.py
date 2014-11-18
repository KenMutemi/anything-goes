from celery.decorators import periodic_task
from celery.task.schedules import crontab
from main.utils.summary_update import update_summaries
from celery.utils.log import get_task_logger
from main.models import Summary

summaries = Summary.objects.all()
logger = get_task_logger(__name__)

@periodic_task(run_every=(crontab(hour=0, minute=30, day_of_week="*")))
def summary_updater():
    for summary in summaries.iterator():
        logger.info("Start task")
        update_summaries(summary)
        logger.info("Task finished: title = %s" % summary.title)
