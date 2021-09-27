from django.urls import path

from transactions.views import entity

urlpatterns = [
    # Entity entity ----
    path('list/', entity.EntityModelListView.as_view(), name='entity-list'),
    path('create/', entity.EntityModelCreateView.as_view(), name='entity-create'),

    # DASHBOARD entity...
    path('<slug:entity_slug>/dashboard/',
         entity.EntityModelDetailView.as_view(),
         name='entity-dashboard'),
    path('<slug:entity_slug>/dashboard/year/<int:year>/',
         entity.FiscalYearEntityModelDashboardView.as_view(),
         name='entity-dashboard-year'),
    path('<slug:entity_slug>/dashboard/quarter/<int:year>/<int:quarter>/',
         entity.QuarterlyEntityDashboardView.as_view(),
         name='entity-dashboard-quarter'),
    path('<slug:entity_slug>/dashboard/month/<int:year>/<int:month>/',
         entity.MonthlyEntityDashboardView.as_view(),
         name='entity-dashboard-month'),
    path('<slug:entity_slug>/dashboard/date/<int:year>/<int:month>/<int:day>/',
         entity.DateEntityDashboardView.as_view(),
         name='entity-dashboard-date'),

    path('<slug:entity_slug>/update/', entity.EntityModelUpdateView.as_view(), name='entity-update'),
    path('<slug:entity_slug>/delete/', entity.EntityDeleteView.as_view(), name='entity-delete'),

    # todo: is this needed?....
    path('<slug:entity_slug>/set-date/', entity.SetSessionDate.as_view(), name='entity-set-date'),

    # todo: is this needed?....
    path('set-default/', entity.SetDefaultEntityView.as_view(), name='entity-set-default'),
]
