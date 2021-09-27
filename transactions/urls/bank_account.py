from django.urls import path

from transactions.views import bank_account

urlpatterns = [
    path('<slug:entity_slug>/list/',
         bank_account.BankAccountModelListView.as_view(),
         name='bank-account-list'),
    path('<slug:entity_slug>/create/',
         bank_account.BankAccountModelCreateView.as_view(),
         name='bank-account-create'),
    path('<slug:entity_slug>/update/<uuid:bank_account_pk>/',
         bank_account.BankAccountModelUpdateView.as_view(),
         name='bank-account-update'),
]
