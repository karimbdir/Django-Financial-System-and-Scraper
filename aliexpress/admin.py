from django.contrib import admin
from .models import AliBabaScraper,AliExpressScraper

# Register your models here.

admin.site.register(AliBabaScraper)
admin.site.register(AliExpressScraper)