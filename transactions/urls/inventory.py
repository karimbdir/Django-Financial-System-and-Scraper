from django.urls import path

from transactions.views import inventory

urlpatterns = [
    path('<slug:entity_slug>/list/',
         inventory.InventoryListView.as_view(),
         name='inventory-list'),
]