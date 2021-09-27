from django.urls import path

from transactions.views import djl_api

urlpatterns = [
    path('entity/<slug:entity_slug>/data/pnl/',
         djl_api.PnLAPIView.as_view(),
         name='entity-json-pnl'),
    path('entity/<slug:entity_slug>/data/net-payables/',
         djl_api.PayableNetAPIView.as_view(),
         name='entity-json-net-payables'),
    path('entity/<slug:entity_slug>/data/net-receivables/',
         djl_api.ReceivableNetAPIView.as_view(),
         name='entity-json-net-receivables'),

    path('unit/<slug:entity_slug>/<slug:unit_slug>/data/pnl/',
         djl_api.PnLAPIView.as_view(),
         name='unit-json-pnl'),
    path('unit/<slug:entity_slug>/<slug:unit_slug>/data/net-payables/',
         djl_api.PayableNetAPIView.as_view(),
         name='unit-json-net-payables'),
    path('unit/<slug:entity_slug>/<slug:unit_slug>/data/net-receivables/',
         djl_api.ReceivableNetAPIView.as_view(),
         name='unit-json-net-receivables'),
]
