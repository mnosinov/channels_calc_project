import os
import django

from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter

import simplecalc.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_calc_project.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            simplecalc.routing.websocet_urlpatterns
        )
    ),
})
