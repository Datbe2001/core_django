import string
import uuid
import random
from datetime import datetime

from django.utils.timezone import make_aware


def generate_code_by_domain(domain='VBL'):
    # Using uuid4 for randomness
    random_part = str(uuid.uuid4())[:8]  # You can adjust the length as needed

    # Adding a random alphanumeric string
    alphanumeric_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

    # Concatenating the two parts
    referral_code = f"{domain}-{random_part}-{alphanumeric_part}"

    return referral_code


def get_quarter_dates(year, quarter):
    if quarter == 1:
        return make_aware(datetime(year, 1, 1)), make_aware(datetime(year, 3, 31, 23, 59, 59, 999999))
    elif quarter == 2:
        return make_aware(datetime(year, 4, 1)), make_aware(datetime(year, 6, 30, 23, 59, 59, 999999))
    elif quarter == 3:
        return make_aware(datetime(year, 7, 1)), make_aware(datetime(year, 9, 30, 23, 59, 59, 999999))
    elif quarter == 4:
        return make_aware(datetime(year, 10, 1)), make_aware(datetime(year, 12, 31, 23, 59, 59, 999999))
