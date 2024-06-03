from django.forms import ModelForm
from .models import ShippingAddress


class ShippingAddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            "line1", "line2", "city", "state", "country", "postal_code", "reference"
        ]

    def __ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields 