from django.urls import re_path

from . import consumers


websocet_urlpatterns = [
    re_path(r'ws/livec/$', consumers.Calculator.as_asgi()),
]
