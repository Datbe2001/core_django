
import logging

import pusher
from django.conf import settings

from core.apps.engine.core.pattern.singleton import Singleton

logger = logging.getLogger(__name__)


class PusherClient(Singleton):
    def __init__(self):
        self.pusher_client = pusher.Pusher(
            app_id=settings.PUSHER_APP_ID,
            key=settings.PUSHER_KEY,
            secret=settings.PUSHER_SECRET,
            cluster=settings.PUSHER_CLUSTER,
            ssl=bool(settings.PUSHER_SSL)
        )

    def push_notification(self, channel, event, data_push):
        try:
            logger.info("PusherClient: push_notification called.")
            self.pusher_client.trigger(channel, event, data_push)
            logger.info("PusherClient: push_notification called successes .")
        except Exception as error:
            logger.error("PusherClient: push_notification error", exc_info=error)