from django.urls import path
from transactions.views import vendor

urlpatterns = [
    path('<slug:entity_slug>/', vendor.VendorModelListView.as_view(), name='vendor-list'),
    path('<slug:entity_slug>/create/', vendor.VendorModelCreateView.as_view(), name='vendor-create'),
    path('<slug:entity_slug>/update/<uuid:vendor_pk>/', vendor.VendorModelUpdateView.as_view(), name='vendor-update'),

]