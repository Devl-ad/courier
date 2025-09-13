from django import forms
from home.models import Package

from basepp import utils


class NewPackageForm(forms.ModelForm):
    sname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Shippers Name",
            }
        ),
        label="Shippers Name",
        required=True,
    )

    scountry = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Shipper Country",
            }
        ),
        label="Shippers Country",
        required=True,
    )
    sphone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Shipper Phone",
            }
        ),
        label="Shippers Phone",
        required=True,
    )

    rphone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Receiver Phone",
            }
        ),
        label="Receiver Phone",
        required=True,
    )

    rname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Receiver Name",
            }
        ),
        label="Receiver Name",
        required=True,
    )
    raddress = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Receiver Address",
            }
        ),
        label="Receiver Address",
        required=True,
    )
    rpostal = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Receiver Postal",
            }
        ),
        label="Receiver Postal",
        required=True,
    )
    remail = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Receiver Email",
            }
        ),
        label="Receiver Email",
        required=True,
    )

    track_id = forms.CharField(
        max_length=8,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "readonly": True,
                "class": "form-control",
            }
        ),
        label="Copy the Track Id",
        required=True,
    )
    origin = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Origin",
            }
        ),
        label="Origin",
        required=True,
    )

    destination = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Destination",
            }
        ),
        label="Destination",
        required=True,
    )

    weight = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "weight",
            }
        ),
        label="weight",
        required=True,
    )

    shipment_mode = forms.CharField(
        widget=forms.Select(
            choices=utils.SHIPMENT_MODE,
            attrs={
                "class": "form-control",
            },
        ),
        label="Shipment Mode",
        required=True,
    )

    carrier_ref_no = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Carrier Ref No",
            }
        ),
        label="Carrier Ref No",
        required=True,
    )

    product = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Product",
            }
        ),
        label="Product",
        required=True,
    )

    quantity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "Quantity",
            }
        ),
        label="Quantity",
        required=True,
    )

    payment_mode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Payment Mode",
            }
        ),
        label="Payment Mode",
        required=True,
    )

    departure_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Departure Date",
            }
        ),
        label="Departure Date",
        required=True,
    )

    expected_delivery_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Expected Delivery Date",
            }
        ),
        label="Expected Delivery Date",
        required=True,
    )

    status = forms.CharField(
        widget=forms.Select(
            choices=utils.STATUS,
            attrs={
                "class": "form-control",
            },
        ),
        label="Status",
        required=True,
    )

    pick_up_date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Pick up Date",
            }
        ),
        label="Pick up Date",
        required=True,
    )

    current_location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Current Location",
            }
        ),
        label="Current Location",
        required=True,
    )

    class Meta:
        model = Package
        fields = [
            "sname",
            "scountry",
            "sphone",
            "rname",
            "rphone",
            "raddress",
            "rpostal",
            "remail",
            "origin",
            "destination",
            "product",
            "weight",
            "quantity",
            "shipment_mode",
            "carrier_ref_no",
            "payment_mode",
            "departure_date",
            "expected_delivery_date",
            "pick_up_date",
            "current_location",
            "status",
            "track_id",
        ]
