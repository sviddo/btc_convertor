from django.urls import path
from .views import (
    subscribe,
    subscribe_api,
    get_rate,
    get_rate_api,
    send_emails,
    send_emails_api,
)

urlpatterns = [
    path('subscribe', subscribe, name='subscribe'),
    path('subscribe_api', subscribe_api, name='subscribe_api'),
    path('rate', get_rate, name='get-rate'),
    path('rate_api', get_rate_api, name='rate-api'),
    path('send_emails', send_emails, name='send-emails'),
    path('send_emails_api', send_emails_api, name='send-emails-api'),
]
