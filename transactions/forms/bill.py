from django.forms import (ModelForm, DateInput, TextInput, Select, CheckboxInput, BaseModelFormSet,
                          modelformset_factory)
from django.utils.translation import gettext_lazy as _

from transactions.io.roles import ASSET_CA_CASH, ASSET_CA_PREPAID, LIABILITY_CL_DEFERRED_REVENUE
from transactions.models import (ItemModel, AccountModel, BillModel, ItemThroughModel,
                                  VendorModel)
from transactions.settings import transactions_FORM_INPUT_CLASSES


class BillModelCreateForm(ModelForm):
    def __init__(self, *args, entity_slug, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.ENTITY_SLUG = entity_slug
        self.USER_MODEL = user_model
        self.get_vendor_queryset()
        self.get_accounts_queryset()

    def get_vendor_queryset(self):

        if 'vendor' in self.fields:
            vendor_qs = VendorModel.objects.for_entity(
                user_model=self.USER_MODEL,
                entity_slug=self.ENTITY_SLUG
            )
            self.fields['vendor'].queryset = vendor_qs

    def get_accounts_queryset(self):

        if all([
            'cash_account' in self.fields,
            'prepaid_account' in self.fields,
            'unearned_account' in self.fields,
        ]):
            account_qs = AccountModel.on_coa.for_bill(
                user_model=self.USER_MODEL,
                entity_slug=self.ENTITY_SLUG
            )

            # forcing evaluation of qs to cache results for fields... (avoids multiple database queries)
            len(account_qs)

            self.fields['cash_account'].queryset = account_qs.filter(role__exact=ASSET_CA_CASH)
            self.fields['prepaid_account'].queryset = account_qs.filter(role__exact=ASSET_CA_PREPAID)
            self.fields['unearned_account'].queryset = account_qs.filter(role__exact=LIABILITY_CL_DEFERRED_REVENUE)

    class Meta:
        model = BillModel
        fields = [
            'vendor',
            'xref',
            'date',
            'terms',
            'cash_account',
            'prepaid_account',
            'unearned_account',
        ]
        widgets = {
            'date': DateInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES,
                'placeholder': _('Bill Date (YYYY-MM-DD)...')
            }),
            'amount_due': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES,
                'placeholder': '$$$'}),
            'xref': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES + ' is-large',
                'placeholder': 'External Reference Number...'}),
            'terms': Select(attrs={
                'class': transactions_FORM_INPUT_CLASSES + ' is-small'
            }),
            'vendor': Select(attrs={
                'class': transactions_FORM_INPUT_CLASSES
            }),

            'cash_account': Select(attrs={'class': transactions_FORM_INPUT_CLASSES}),
            'prepaid_account': Select(attrs={'class': transactions_FORM_INPUT_CLASSES}),
            'unearned_account': Select(attrs={'class': transactions_FORM_INPUT_CLASSES}),
        }


class BillModelUpdateForm(BillModelCreateForm):

    def save(self, commit=True):
        if commit:
            self.instance.migrate_state(
                user_model=self.USER_MODEL,
                entity_slug=self.ENTITY_SLUG
            )
        super().save(commit=commit)

    class Meta:
        model = BillModel
        fields = [
            'xref',
            'amount_due',
            'amount_paid',
            'paid',
            'paid_date',
            'progress',
            'accrue'
        ]
        widgets = {
            'xref': TextInput(attrs={'class': transactions_FORM_INPUT_CLASSES,
                                     'placeholder': 'External Reference...'}),
            'date': DateInput(attrs={'class': transactions_FORM_INPUT_CLASSES}),
            'amount_due': TextInput(attrs={'class': transactions_FORM_INPUT_CLASSES, 'placeholder': '$$$'}),
            'terms': Select(attrs={'class': transactions_FORM_INPUT_CLASSES}),
            'paid_date': DateInput(
                attrs={
                    'class': transactions_FORM_INPUT_CLASSES,
                    'placeholder': _('Date (YYYY-MM-DD)...')}
            ),
            'amount_paid': TextInput(
                attrs={
                    'class': transactions_FORM_INPUT_CLASSES,
                }),
            'progress': TextInput(attrs={'class': transactions_FORM_INPUT_CLASSES}),
            'accrue': CheckboxInput(attrs={'type': 'checkbox'}),
            'paid': CheckboxInput(attrs={'type': 'checkbox'}),
            'cash_account': Select(attrs={'class': transactions_FORM_INPUT_CLASSES + ' is-danger'}),
            'prepaid_account': Select(attrs={'class': transactions_FORM_INPUT_CLASSES + ' is-danger'}),
            'unearned_account': Select(attrs={'class': transactions_FORM_INPUT_CLASSES + ' is-danger'}),
        }


class BillModelConfigureForm(BillModelUpdateForm):
    class Meta(BillModelUpdateForm.Meta):
        fields = [
            'xref',
            'amount_due',
            'amount_paid',
            'paid',
            'paid_date',
            'progress',
            'accrue',
            'cash_account',
            'prepaid_account',
            'unearned_account',
        ]


class BillItemForm(ModelForm):
    class Meta:
        model = ItemThroughModel
        fields = [
            'item_model',
            'unit_cost',
            'entity_unit',
            'quantity'
        ]
        widgets = {
            'item_model': Select(attrs={
                'class': transactions_FORM_INPUT_CLASSES,
            }),
            'entity_unit': Select(attrs={
                'class': transactions_FORM_INPUT_CLASSES,
            }),
            'unit_cost': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES,
            }),
            'quantity': TextInput(attrs={
                'class': transactions_FORM_INPUT_CLASSES,
            })
        }


class BaseBillItemFormset(BaseModelFormSet):

    def __init__(self, *args, entity_slug, bill_pk, user_model, **kwargs):
        super().__init__(*args, **kwargs)
        self.USER_MODEL = user_model
        self.BILL_PK = bill_pk
        self.ENTITY_SLUG = entity_slug

        items_qs = ItemModel.objects.for_bill(
            entity_slug=self.ENTITY_SLUG,
            user_model=self.USER_MODEL
        )

        for form in self.forms:
            form.fields['item_model'].queryset = items_qs


BillItemFormset = modelformset_factory(
    model=ItemThroughModel,
    form=BillItemForm,
    formset=BaseBillItemFormset,
    can_delete=True,
    extra=5
)
