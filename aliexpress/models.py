from django.db import models

# Create your models here.

class AliBabaScraper(models.Model):
    product_id = models.IntegerField()
    title = models.CharField(max_length=500,blank=True,null=True)
    price_from = models.FloatField(blank=True,null=True)
    price_to = models.FloatField(blank=True,null=True)
    link = models.URLField(blank=True,null=True)
    product_search = models.CharField(max_length=500,blank=True,null=True)
    product_score = models.FloatField(blank=True,null=True)
    review_count = models.IntegerField(blank=True,null=True)
    review_score = models.FloatField(blank=True,null=True)
    shipping_time = models.FloatField(blank=True,null=True)
    supplier_service = models.FloatField(blank=True,null=True)
    supplier_name = models.CharField(max_length=500,blank=True,null=True)
    supplier_link = models.URLField(blank=True,null=True)
    supplier_year = models.IntegerField(null=True,blank=True)
    supplier_country = models.CharField(max_length=500,blank=True,null=True)
    min_order = models.CharField(max_length=500,blank=True,null=True)

    class Meta:
        verbose_name_plural = 'Ali Baba'

    def __str__(self):
        return f'ID: {self.product_id} - Product Name: {self.title} - Search: {self.product_search}'

    
class AliExpressScraper(models.Model):
    product_id = models.IntegerField()
    title = models.CharField(max_length=500,blank=True,null=True)
    price = models.FloatField(null=True, blank=True)
    unit = models.CharField(max_length=500,blank=True,null=True)
    rating = models.FloatField(blank=True,null=True)
    supplier_name = models.CharField(max_length=500,blank=True,null=True)
    supplier_link = models.URLField(null=True, blank=True)
    product_search = models.CharField(max_length=500,blank=True,null=True)

    
    class Meta:
        verbose_name_plural = 'Ali Express'

    def __str__(self):
        return f'ID: {self.product_id} - Product Name: {self.title} - Search: {self.product_search}'