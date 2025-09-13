from django.db import models
from basepp import utils


class Package(models.Model):
    # Shipper
    sname = models.CharField(max_length=400, blank=True, null=True)
    scountry = models.CharField(max_length=400, blank=True, null=True)
    sphone = models.CharField(max_length=400, blank=True, null=True)
    # Receiver
    rname = models.CharField(max_length=400, blank=True, null=True)
    raddress = models.CharField(max_length=400, blank=True, null=True)
    rphone = models.CharField(max_length=400, blank=True, null=True)
    rpostal = models.CharField(max_length=400, blank=True, null=True)
    remail = models.CharField(max_length=400, blank=True, null=True)
    # <Receiver>

    origin = models.CharField(max_length=400, blank=True, null=True)

    track_id = models.CharField(unique=True, max_length=10)
    status = models.CharField(max_length=400, choices=utils.STATUS, default=utils.PD)
    destination = models.CharField(max_length=400, blank=True, null=True)
    weight = models.CharField(max_length=400, blank=True, null=True)
    shipment_mode = models.CharField(
        max_length=400, choices=utils.SHIPMENT_MODE, default="Air freight"
    )
    carrier_ref_no = models.CharField(max_length=400, blank=True, null=True)
    product = models.CharField(max_length=400, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    payment_mode = models.CharField(max_length=400, blank=True, null=True)
    departure_date = models.CharField(max_length=400, blank=True, null=True)
    expected_delivery_date = models.CharField(max_length=400, blank=True, null=True)
    pick_up_date = models.CharField(max_length=400, blank=True, null=True)
    current_location = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return f"{self.track_id}"
