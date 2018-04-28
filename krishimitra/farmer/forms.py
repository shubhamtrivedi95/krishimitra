from django import forms

from . models import client
class GetData(forms.ModelForm):
    class Meta:
        model=client
        fields=[
            'CustmerName',
            'MobileNo',
            'DeviceId',
        ]