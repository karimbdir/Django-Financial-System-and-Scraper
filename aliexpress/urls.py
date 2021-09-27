from django.urls import path
from . import views
app_name = 'scraper'

urlpatterns = [
    path('add-alibaba',views.scrape_alibaba,name="scrape-alibaba"),
    path('alibaba_list',views.AliBabaListView.as_view(), name="alibaba_list"),
    path('alibaba_detail/<pk>',views.AliBabaDetailView.as_view(), name="alibaba_detail"),
    path('alibaba_delete/<pk>',views.AliBabaDeleteView.as_view(), name="alibaba_delete"),
    path('add-aliexpress',views.scrape_aliexpress,name="scrape-aliexpress"),
    path('aliexpress_list',views.AliExpressListView.as_view(), name="aliexpress_list"),
    path('aliexpress_detail/<pk>',views.AliExpressDetailView.as_view(), name="aliexpress_detail"),
    path('aliexpress_delete/<pk>',views.AliExpressDeleteView.as_view(), name="aliexpress_delete"),
]
