from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from transactions.forms.journal_entry import JournalEntryModelUpdateForm, JournalEntryModelCreateForm
from transactions.models.journalentry import JournalEntryModel
from transactions.models.ledger import LedgerModel
from transactions.views.mixins import LoginRequiredMixIn


# JE Views ---
class JournalEntryListView(LoginRequiredMixIn, ListView):
    context_object_name = 'journal_entries'
    template_name = 'transactions/je_list.html'
    PAGE_TITLE = _('Journal Entries')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE
    }

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        if not sort:
            sort = '-updated'
        return JournalEntryModel.on_coa.for_ledger(
            ledger_pk=self.kwargs['ledger_pk'],
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by(sort)


class JournalEntryDetailView(LoginRequiredMixIn, DetailView):
    context_object_name = 'journal_entry'
    template_name = 'transactions/je_detail.html'
    slug_url_kwarg = 'je_pk'
    slug_field = 'uuid'
    PAGE_TITLE = _('Journal Entry Detail')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:journal-plus'
    }

    def get_queryset(self):
        return JournalEntryModel.on_coa.for_ledger(
            entity_slug=self.kwargs['entity_slug'],
            ledger_pk=self.kwargs['ledger_pk'],
            user_model=self.request.user
        ).prefetch_related('txs', 'txs__account')


class JournalEntryUpdateView(LoginRequiredMixIn, UpdateView):
    context_object_name = 'journal_entry'
    template_name = 'transactions/je_update.html'
    slug_url_kwarg = 'je_pk'
    PAGE_TITLE = _('Update Journal Entry')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE
    }

    def get_slug_field(self):
        return 'uuid'

    def get_form(self, form_class=None):
        return JournalEntryModelUpdateForm(
            entity_slug=self.kwargs['entity_slug'],
            ledger_pk=self.kwargs['ledger_pk'],
            user_model=self.request.user,
            **self.get_form_kwargs()
        )

    def get_success_url(self):
        return reverse('transactions:je-list', kwargs={
            'entity_slug': self.kwargs['entity_slug'],
            'ledger_pk': self.kwargs['ledger_pk']
        })

    def get_queryset(self):
        return JournalEntryModel.on_coa.for_ledger(
            entity_slug=self.kwargs['entity_slug'],
            ledger_pk=self.kwargs['ledger_pk'],
            user_model=self.request.user
        ).prefetch_related('txs', 'txs__account')


class JournalEntryCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'transactions/je_create.html'
    PAGE_TITLE = _('Create Journal Entry')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE
    }

    def get_form(self, form_class=None):
        return JournalEntryModelCreateForm(
            entity_slug=self.kwargs['entity_slug'],
            ledger_pk=self.kwargs['ledger_pk'],
            user_model=self.request.user,
            **self.get_form_kwargs()
        )

    def form_valid(self, form):
        ledger_model = LedgerModel.objects.for_entity(
            user_model=self.request.user,
            entity_slug=self.kwargs['entity_slug'],
        ).get(uuid__exact=self.kwargs['ledger_pk'])
        form.instance.ledger = ledger_model
        self.object = form.save()
        return super().form_valid(form)

    def get_initial(self):
        return {
            'ledger': LedgerModel.objects.for_entity(
                entity_slug=self.kwargs['entity_slug'],
                user_model=self.request.user
            ).get(uuid__exact=self.kwargs['ledger_pk'])
        }

    def get_success_url(self):
        return reverse('transactions:je-list',
                       kwargs={
                           'entity_slug': self.kwargs.get('entity_slug'),
                           'ledger_pk': self.kwargs.get('ledger_pk')
                       })
