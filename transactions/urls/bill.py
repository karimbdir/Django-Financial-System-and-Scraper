from django.urls import path

from transactions.views import bill

urlpatterns = [
    path('<slug:entity_slug>/latest/',
         bill.BillModelListView.as_view(),
         name='bill-list'),
    path('<slug:entity_slug>/year/<int:year>/',
         bill.BillModelYearListView.as_view(),
         name='bill-list-year'),
    path('<slug:entity_slug>/month/<int:year>/<int:month>/',
         bill.BillModelMonthListView.as_view(),
         name='bill-list-month'),
    path('<slug:entity_slug>/create/',
         bill.BillModelCreateView.as_view(),
         name='bill-create'),
    path('<slug:entity_slug>/create/purchase-order/<uuid:po_pk>/',
         bill.BillModelCreateView.as_view(for_purchase_order=True),
         name='bill-create-po'),
    path('<slug:entity_slug>/detail/<uuid:bill_pk>/',
         bill.BillModelDetailView.as_view(),
         name='bill-detail'),
    path('<slug:entity_slug>/update/<uuid:bill_pk>/',
         bill.BillModelUpdateView.as_view(),
         name='bill-update'),
    path('<slug:entity_slug>/update/<uuid:bill_pk>/items/',
         bill.BillModelItemsUpdateView.as_view(),
         name='bill-update-items'),
    path('<slug:entity_slug>/delete/<uuid:bill_pk>/',
         bill.BillModelDeleteView.as_view(),
         name='bill-delete'),
    path('<slug:entity_slug>/mark-as-paid/<uuid:bill_pk>/',
         bill.BillModelMarkPaidView.as_view(),
         name='bill-mark-paid'),
    path('<slug:entity_slug>/void/<uuid:bill_pk>/',
         bill.BillModelDeleteView.as_view(void=True),
         name='bill-void'),

    # actions....
    path('<slug:entity_slug>/actions/<uuid:bill_pk>/force-migrate/',
         bill.BillModelActionView.as_view(
             action=bill.BillModelActionView.ACTION_FORCE_MIGRATE),
         name='bill-action-force-migrate'),
    path('<slug:entity_slug>/actions/<uuid:bill_pk>/lock/',
         bill.BillModelActionView.as_view(
             action=bill.BillModelActionView.ACTION_LOCK),
         name='bill-action-lock'),
    path('<slug:entity_slug>/actions/<uuid:bill_pk>/unlock/',
         bill.BillModelActionView.as_view(
             action=bill.BillModelActionView.ACTION_UNLOCK),
         name='bill-action-unlock'),
]
