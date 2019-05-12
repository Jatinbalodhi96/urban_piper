from django.conf.urls import url

from . import consumer


websocket_url_pattern = [
    url('connect', consumer.BroadCastConsumer),
]