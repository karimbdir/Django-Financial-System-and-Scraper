from django.forms import ModelForm, TextInput, EmailInput

from transactions.forms.utils import validate_cszc
from transactions.models.vendor import VendorModel
from transactions.settings import transactions_FORM_INPUT_CLASSES


class VendorModelForm(ModelForm):

    def clean(self):
        validate_cszc(self.cleaned_data)

    class Meta:
        model = VendorModel
        fields = [
            'vendor_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'country',
            'phone',
            'email',
            'website',
        ]
        widgets = {
            'vendor_name': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'address_1': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'address_2': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'city': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'state': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'zip_code': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'country': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'phone': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'email': EmailInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'website': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
        }
