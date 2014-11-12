from celery.task.schedules import crontab
from celery.decorators import periodic_task
from main.utils.summary_update import update_summaries
from celery.utils.log import get_task_logger
from main.models import Summary
summaries = Summary.objects.all()

logger = get_task_logger(__name__)

# A periodic task that will run every minute (the symbol "*" means every)
@periodic_task(run_every=(crontab(hour=21, minute=30, day_of_week="*")))
def summary_updater():
    for summary in summaries:
        logger.info("Start task")
        update_summaries(summary)
        logger.info("Task finished: title = %s" % summary.title)
