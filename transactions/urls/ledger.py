from django.urls import path
from transactions.views import ledger

urlpatterns = [
    path('<slug:entity_slug>/list/', ledger.LedgerModelListView.as_view(), name='ledger-list'),
    path('<slug:entity_slug>/create/', ledger.LedgerModelCreateView.as_view(), name='ledger-create'),
    path('<slug:entity_slug>/update/<uuid:ledger_pk>/', ledger.LedgerModelUpdateView.as_view(), name='ledger-update'),
]
