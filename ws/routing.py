from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("v1/sync", consumers.SyncConsumer.as_asgi()),
]
