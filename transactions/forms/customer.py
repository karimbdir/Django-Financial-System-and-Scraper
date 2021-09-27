from django.forms import ModelForm, TextInput, EmailInput

from transactions.forms.utils import validate_cszc
from transactions.models.customer import CustomerModel
from transactions.settings import transactions_FORM_INPUT_CLASSES


class CustomerModelForm(ModelForm):

    def clean(self):
        validate_cszc(self.cleaned_data)

    class Meta:
        model = CustomerModel
        fields = [
            'customer_name',
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
            'customer_name': TextInput(attrs={
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
                'class': transactions_FORM_INPUT_CLASSES,
            }),
            'phone': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES,
            }),
            'email': EmailInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'website': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
        }