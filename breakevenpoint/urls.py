from django.urls import path
from . import views

app_name = 'breakevenpoint'

urlpatterns = [
    path('bep_list',views.BEPListView.as_view(), name="bep_list"),
    path('bep_detail/<pk>',views.BEPDetailView.as_view(), name="bep_detail"),
    path('bep_create',views.BEPCreateView.as_view(), name="bep_create"),
    path('bep_update/<pk>',views.BEPUpdateView.as_view(), name="bep_update"),
    path('bep_delete/<pk>',views.BEPDeleteView.as_view(), name="bep_delete"),
]