from django.urls import path

from transactions.views import account

urlpatterns = [
    path('<slug:entity_slug>/list/',
         account.AccountModelListView.as_view(),
         name='account-list'),
    path('<slug:entity_slug>/create/',
         account.AccountModelCreateView.as_view(),
         name='account-create'),
    path('<slug:entity_slug>/create-child-account/<uuid:parent_account_pk>/',
         account.AccountModelCreateChildView.as_view(),
         name='account-create-child'),
    path('<slug:entity_slug>/update/<uuid:account_pk>/',
         account.AccountModelUpdateView.as_view(),
         name='account-update'),
    path('<slug:entity_slug>/detail/<uuid:account_pk>/',
         account.AccountModelDetailView.as_view(),
         name='account-detail'),
    path('<slug:entity_slug>/detail/<uuid:account_pk>/year/<int:year>/',
         account.AccountModelYearDetailView.as_view(),
         name='account-detail-year'),
    path('<slug:entity_slug>/detail/<uuid:account_pk>/quarter/<int:year>/<int:quarter>/',
         account.AccountModelQuarterDetailView.as_view(),
         name='account-detail-quarter'),
    path('<slug:entity_slug>/detail/<uuid:account_pk>/month/<int:year>/<int:month>/',
         account.AccountModelMonthDetailView.as_view(),
         name='account-detail-month'),
    path('<slug:entity_slug>/detail/<uuid:account_pk>/date/<int:year>/<int:month>/<int:day>/',
         account.AccountModelDateDetailView.as_view(),
         name='account-detail-date')
]
