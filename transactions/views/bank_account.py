from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from transactions.forms.bank_account import BankAccountCreateForm, BankAccountUpdateForm
from transactions.models.bank_account import BankAccountModel
from transactions.utils import new_bankaccount_protocol
from transactions.views.mixins import LoginRequiredMixIn


class BankAccountModelListView(LoginRequiredMixIn, ListView):
    template_name = 'transactions/bank_account_list.html'
    PAGE_TITLE = _('Bank Accounts')
    context_object_name = 'bank_accounts'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'clarity:bank-line'
    }

    def get_queryset(self):
        return BankAccountModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('cash_account')


class BankAccountModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'transactions/bank_account_create.html'
    form_class = BankAccountCreateForm
    PAGE_TITLE = _('Create Bank Account')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'clarity:bank-line'
    }

    def get_form(self, form_class=None):
        return BankAccountCreateForm(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            **self.get_form_kwargs()
        )

    def get_success_url(self):
        return reverse('transactions:bank-account-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        bank_account_model: BankAccountModel = form.save(commit=False)
        new_bankaccount_protocol(
            bank_account_model=bank_account_model,
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user)
        bank_account_model.save()
        return HttpResponseRedirect(self.get_success_url())


class BankAccountModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'transactions/bank_account_update.html'
    pk_url_kwarg = 'bank_account_pk'
    PAGE_TITLE = _('Update Bank Account')
    context_object_name = 'bank_account'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'clarity:bank-line'
    }

    def get_success_url(self):
        return reverse('transactions:bank-account-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def get_queryset(self):
        return BankAccountModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).select_related('ledger')

    def get_form(self, form_class=None):
        return BankAccountUpdateForm(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user,
            **self.get_form_kwargs()
        )
