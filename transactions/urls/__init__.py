from django.urls import path, include

from transactions.views import home

app_name = 'transactions'

urlpatterns = [

    path('entity/', include('transactions.urls.entity')),
    path('unit/', include('transactions.urls.unit')),
    path('report/', include('transactions.urls.report')),
    path('chart-of-accounts/', include('transactions.urls.chart_of_accounts')),
    path('account/', include('transactions.urls.account')),
    path('ledger/', include('transactions.urls.ledger')),
    path('journal-entry/', include('transactions.urls.journal_entry')),
    path('transactions/', include('transactions.urls.transactions')),
    path('invoice/', include('transactions.urls.invoice')),
    path('bill/', include('transactions.urls.bill')),
    path('purchase_order/', include('transactions.urls.purchase_order')),
    path('customer/', include('transactions.urls.customer')),
    path('vendor/', include('transactions.urls.vendor')),
    path('item/', include('transactions.urls.item')),
    path('bank-account/', include('transactions.urls.bank_account')),
    path('data-import/', include('transactions.urls.data_import')),
    path('feedback/', include('transactions.urls.feedback')),
    path('inventory/', include('transactions.urls.inventory')),
    path('home/', include('transactions.urls.home')),
    path('djl-api/v1/', include('transactions.urls.djl_api')),
    path('', home.RootUrlView.as_view(), name='root'),
]