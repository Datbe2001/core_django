import random
from datetime import timedelta, date, datetime

from django.conf import settings
from django.utils import timezone
from django.db import transaction
from django.core.mail import send_mail
from django.utils.html import strip_tags

from rest_framework import serializers
from rest_framework.response import Response

from core.apps.engine.utils.utils import *
from core.apps.engine.utils.constant import *
from core.apps.engine.models import (
    User
)
