from django.urls import path

from transactions.views import data_import

urlpatterns = [
    path('<slug:entity_slug>/jobs/',
         data_import.DataImportJobsListView.as_view(),
         name='data-import-jobs-list'),
    path('<slug:entity_slug>/import-ofx/',
         data_import.DataImportOFXFileView.as_view(),
         name='data-import-ofx'),
    path('<slug:entity_slug>/jobs/<uuid:job_pk>/txs/',
         data_import.DataImportJobDetailView.as_view(),
         name='data-import-job-txs'),
]
