from celery import Celery
from email_sender import send_email
from config import Config

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
celery.conf.update(result_backend=Config.CELERY_RESULT_BACKEND)

@celery.task
def schedule_email(email_data):
    # Logic to retrieve email details from `email_data`
    send_email(to_email=email_data['to'], subject=email_data['subject'], content=email_data['content'])
