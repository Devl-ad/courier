from uuid import uuid4

from django.conf import settings


EMAIL_ADMIN = settings.DEFAULT_FROM_EMAIL


def gen_random_ids():
    code = str(uuid4()).replace(" ", "-").upper()[:8]
    return code


PD = "PENDING"
DV = "DELIVERD"


STATUS = (
    ("PENDING", "PENDING"),
    ("Out For Delivery", "Out For Delivery"),
    ("DELIVERD", "DELIVERD"),
)

SHIPMENT_MODE = (
    ("Air freight", "Air freight"),
    ("ocean freight", "ocean freight"),
    ("cargo express", "cargo express"),
)
