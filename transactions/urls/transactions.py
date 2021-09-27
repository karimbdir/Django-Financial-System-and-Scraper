from django.urls import path

from transactions.views import transactions

urlpatterns = [
    path('txs/<slug:entity_slug>/<uuid:ledger_pk>/journal-entry/<uuid:je_pk>/',
         transactions.TXSJournalEntryView.as_view(),
         name='txs-journal-entry'),
]
