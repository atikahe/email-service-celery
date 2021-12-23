from requests import ConnectionError, RequestException
from logging import getLogger
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

logger = getLogger('queue')

@shared_task()
def send_email_task():
    subject = 'CELERY TASK WORKED CCHECK AFTER ADDING BROKER!'
    body = 'This is proof that celery task is running'
    from_address = settings.DEFAULT_FROM_EMAIL
    to_address = ['gimibon673@revutap.com']
    # sleep(10)
    send_mail(subject, body, from_address, to_address)
    return None


