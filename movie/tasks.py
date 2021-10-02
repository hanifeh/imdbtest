from celery import Celery
from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from movie import models
from datetime import date

app = Celery('celery_tasks', broker='pyamqp://guest@localhost//', backend='rpc://',)

