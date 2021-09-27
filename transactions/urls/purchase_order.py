from django.urls import path

from transactions.views import purchase_order

urlpatterns = [
    path('<slug:entity_slug>/latest/',
         purchase_order.PurchaseOrderModelListView.as_view(),
         name='po-list'),
    path('<slug:entity_slug>/year/<int:year>/',
         purchase_order.PurchaseOrderModelYearListView.as_view(),
         name='po-list-year'),
    path('<slug:entity_slug>/month/<int:year>/<int:month>/',
         purchase_order.PurchaseOrderModelMonthListView.as_view(),
         name='po-list-month'),
    path('<slug:entity_slug>/create/',
         purchase_order.PurchaseOrderModelCreateView.as_view(),
         name='po-create'),
    path('<slug:entity_slug>/detail/<uuid:po_pk>/',
         purchase_order.PurchaseOrderModelDetailView.as_view(),
         name='po-detail'),
    path('<slug:entity_slug>/update/<uuid:po_pk>/',
         purchase_order.PurchaseOrderModelUpdateView.as_view(),
         name='po-update'),
    path('<slug:entity_slug>/update/<uuid:po_pk>/update-items/',
         purchase_order.PurchaseOrderModelUpdateView.as_view(update_items=True),
         name='po-update-items'),
    path('<slug:entity_slug>/delete/<uuid:po_pk>/',
         purchase_order.PurchaseOrderModelDeleteView.as_view(),
         name='po-delete'),
    # path('<slug:entity_slug>/mark-as-paid/<uuid:bill_pk>/',
    #      views.BillModelMarkPaidView.as_view(),
    #      name='bill-mark-paid'),
]
