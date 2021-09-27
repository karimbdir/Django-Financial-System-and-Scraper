from django.urls import path
from transactions.views import customer

urlpatterns = [
    path('<slug:entity_slug>/list/', customer.CustomerModelListView.as_view(), name='customer-list'),
    path('<slug:entity_slug>/create/', customer.CustomerModelCreateView.as_view(), name='customer-create'),
    path('<slug:entity_slug>/update/<uuid:customer_pk>/',
         customer.CustomerModelUpdateView.as_view(),
         name='customer-update'),
]
