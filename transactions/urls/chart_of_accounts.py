from django.urls import path

from transactions.views import coa

urlpatterns = [
    path('<slug:entity_slug>/<slug:coa_slug>/update/', coa.ChartOfAccountsUpdateView.as_view(), name='coa-update'),
]
