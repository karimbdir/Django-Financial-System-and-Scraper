from django.urls import path

from transactions.views import journal_entry

urlpatterns = [
    path('<slug:entity_slug>/<uuid:ledger_pk>/list/',
         journal_entry.JournalEntryListView.as_view(),
         name='je-list'),
    path('<slug:entity_slug>/<uuid:ledger_pk>/create/',
         journal_entry.JournalEntryCreateView.as_view(),
         name='je-create'),
    path('<slug:entity_slug>/<uuid:ledger_pk>/detail/<uuid:je_pk>/',
         journal_entry.JournalEntryDetailView.as_view(),
         name='je-detail'),
    path('<slug:entity_slug>/<uuid:ledger_pk>/update/<uuid:je_pk>/',
         journal_entry.JournalEntryUpdateView.as_view(),
         name='je-update'),
]
