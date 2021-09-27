from django.urls import path

from transactions.views import unit,entity

urlpatterns = [
    path('<slug:entity_slug>/unit/list/',
         unit.EntityUnitModelListView.as_view(),
         name='unit-list'),
    path('<slug:entity_slug>/detail/<slug:unit_slug>/',
         unit.EntityUnitModelDetailView.as_view(),
         name='unit-detail'),
    path('<slug:entity_slug>/unit/create/',
         unit.EntityUnitModelCreateView.as_view(),
         name='unit-create'),
    path('<slug:entity_slug>/unit/update/<slug:unit_slug>/',
         unit.EntityUnitUpdateView.as_view(),
         name='unit-update'),


    # DASHBOARD unit ...
    path('<slug:entity_slug>/dashboard/<slug:unit_slug>/',
         entity.EntityModelDetailView.as_view(),
         name='unit-dashboard'),
    path('<slug:entity_slug>/dashboard/<slug:unit_slug>/year/<int:year>/',
         entity.FiscalYearEntityModelDashboardView.as_view(),
         name='unit-dashboard-year'),
    path('<slug:entity_slug>/dashboard/<slug:unit_slug>/quarter/<int:year>/<int:quarter>/',
         entity.QuarterlyEntityDashboardView.as_view(),
         name='unit-dashboard-quarter'),
    path('<slug:entity_slug>/dashboard/<slug:unit_slug>/month/<int:year>/<int:month>/',
         entity.MonthlyEntityDashboardView.as_view(),
         name='unit-dashboard-month'),
    path('<slug:entity_slug>/dashboard/<slug:unit_slug>/date/<int:year>/<int:month>/<int:day>/',
         entity.DateEntityDashboardView.as_view(),
         name='unit-dashboard-date'),

]
