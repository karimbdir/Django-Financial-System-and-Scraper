from django.urls import path

from transactions.views import home

urlpatterns = [
    path('my-dashboard/', home.DasboardView.as_view(), name='home'),
]
