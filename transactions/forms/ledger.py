from django.forms import ModelForm, TextInput, Select

from transactions.models.ledger import LedgerModel
from transactions.settings import transactions_FORM_INPUT_CLASSES


class LedgerModelCreateForm(ModelForm):

    def __init__(self, entity_slug: str, user_model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG: str = entity_slug
        self.USER_MODEL = user_model

    class Meta:
        model = LedgerModel
        fields = [
            'name',
            # 'unit'
        ]
        widgets = {
            'name': TextInput(
                attrs={
                    'class': transactions_FORM_INPUT_CLASSES
                }
            ),
        }


class LedgerModelUpdateForm(LedgerModelCreateForm):
    class Meta:
        model = LedgerModel
        fields = [
            'name',
            # 'unit',
            'posted',
            'locked',
        ]
        widgets = {
            'name': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
            'entity_unit': Select(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),
        }