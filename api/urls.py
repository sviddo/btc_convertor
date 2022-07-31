from django.urls import path
from .views import (
    subscribe,
    subscribe_api,
)

urlpatterns = [
    path('subscribe', subscribe, name='subscribe'),
    path('subscribe_api', subscribe_api, name='subscribe_api'),
]
