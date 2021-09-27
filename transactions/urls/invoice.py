from django.urls import path

from transactions.views import invoice

urlpatterns = [
    path('<slug:entity_slug>/lastest/',
         invoice.InvoiceModelListView.as_view(),
         name='invoice-list'),
    path('<slug:entity_slug>/year/<int:year>/',
         invoice.InvoiceModelYearlyListView.as_view(),
         name='invoice-list-year'),
    path('<slug:entity_slug>/month/<int:year>/<int:month>/',
         invoice.InvoiceModelMonthlyListView.as_view(),
         name='invoice-list-month'),
    path('<slug:entity_slug>/create/',
         invoice.InvoiceModelCreateView.as_view(),
         name='invoice-create'),
    path('<slug:entity_slug>/detail/<uuid:invoice_pk>/',
         invoice.InvoiceModelDetailView.as_view(),
         name='invoice-detail'),
    path('<slug:entity_slug>/update/<uuid:invoice_pk>/',
         invoice.InvoiceModelUpdateView.as_view(),
         name='invoice-update'),
    path('<slug:entity_slug>/update/<uuid:invoice_pk>/items/',
         invoice.InvoiceModelItemsUpdateView.as_view(),
         name='invoice-update-items'),
    path('<slug:entity_slug>/delete/<uuid:invoice_pk>/',
         invoice.InvoiceModelDeleteView.as_view(),
         name='invoice-delete'),
    path('<slug:entity_slug>/mark-as-paid/<uuid:invoice_pk>/',
         invoice.InvoiceModelMarkPaidView.as_view(),
         name='invoice-mark-paid'),

    # actions....
    path('<slug:entity_slug>/actions/<uuid:invoice_pk>/force-migrate/',
         invoice.InvoiceModelActionView.as_view(
             action=invoice.InvoiceModelActionView.ACTION_FORCE_MIGRATE),
         name='invoice-action-force-migrate'),
    path('<slug:entity_slug>/actions/<uuid:invoice_pk>/lock/',
         invoice.InvoiceModelActionView.as_view(
             action=invoice.InvoiceModelActionView.ACTION_LOCK),
         name='invoice-action-lock'),
    path('<slug:entity_slug>/actions/<uuid:invoice_pk>/unlock/',
         invoice.InvoiceModelActionView.as_view(
             action=invoice.InvoiceModelActionView.ACTION_UNLOCK),
         name='invoice-action-unlock'),

]
