from django.urls import path

from transactions.views import item

urlpatterns = [
    path('<str:entity_slug>/list/uom/', item.UnitOfMeasureModelListView.as_view(), name='uom-list'),
    path('<str:entity_slug>/create/uom/', item.UnitOfMeasureModelCreateView.as_view(), name='uom-create'),
    path('<str:entity_slug>/update/uom/<uuid:uom_pk>/', item.UnitOfMeasureModelUpdateView.as_view(), name='uom-update'),

    # todo: rename url to product-item-XXX
    path('<str:entity_slug>/list/product/', item.ProductsAndServicesListView.as_view(), name='product-list'),
    path('<str:entity_slug>/create/product/', item.ProductOrServiceCreateView.as_view(), name='product-create'),
    path('<str:entity_slug>/update/product/<uuid:item_pk>/',
         item.ProductOrServiceUpdateView.as_view(),
         name='product-update'),

    # todo: rename url to expense-item-XXX
    path('<str:entity_slug>/list/expense/', item.ExpenseItemModelListView.as_view(), name='expense-list'),
    path('<str:entity_slug>/create/expense/', item.ExpenseItemCreateView.as_view(), name='expense-create'),
    path('<str:entity_slug>/update/expense/<uuid:item_pk>/',
         item.ExpenseItemUpdateView.as_view(),
         name='expense-update'),

    path('<str:entity_slug>/list/inventory/', item.InventoryItemModelListView.as_view(), name='inventory-item-list'),
    path('<str:entity_slug>/create/inventory/', item.InventoryItemCreateView.as_view(), name='inventory-item-create'),
    path('<str:entity_slug>/update/inventory/<uuid:item_pk>/',
         item.InventoryItemUpdateView.as_view(),
         name='inventory-item-update'),

]
