from django.db import models

# Create your models here.

class CalculateBEP(models.Model):
    project_title = models.CharField(max_length=100)
    sales = models.FloatField(default=0,blank=True,null=True)
    units_sold = models.IntegerField(default=0)
    sales_per_unit = models.FloatField(blank=True,null=True)
    variable_cost = models.FloatField(default=0)
    vc_per_unit = models.FloatField(blank=True,null=True)
    contribution_margin = models.FloatField(default=0,blank=True,null=True)
    contribution_margin_per_unit = models.FloatField(blank=True,null=True)
    contrubtion_margin_pct = models.FloatField(default=0,blank=True,null=True)
    fixed_cost = models.FloatField(default=0)
    net_income = models.FloatField(blank=True,null=True)
    breakevendollar = models.FloatField(blank=True,null=True)
    breakevenunit = models.FloatField(blank=True,null=True)
    margin_safety = models.FloatField(blank=True,null=True)
    target_profit = models.FloatField(default=0)
    targetbepd = models.FloatField(blank=True,null=True)
    targetbepu = models.FloatField(blank=True,null=True)


    def __str__(self):
        return f'ProjectID {self.id} Project: {self.project_title} '


    def save(self, *args, **kwargs):
        if self.sales == 0:
            self.sales = (self.contribution_margin / (self.contrubtion_margin_pct / 100))
        if self.contribution_margin == 0:
            self.contribution_margin = (self.sales * (self.contrubtion_margin_pct /100))
        else:
            self.contribution_margin = self.sales - self.variable_cost
        self.net_income = self.contribution_margin - self.fixed_cost
        self.sales_per_unit = self.sales / self.units_sold
        self.vc_per_unit = self.variable_cost / self.units_sold
        self.contribution_margin_per_unit = self.contribution_margin / self.units_sold
        if self.contrubtion_margin_pct == 0:
            self.contribution_margin_pct = (self.contribution_margin / self.sales) * 100
        self.breakevendollar = (self.fixed_cost / (self.contrubtion_margin_pct / 100))
        self.breakevenunit = self.fixed_cost / self.contrubtion_margin_pct
        self.margin_safety = self.sales - self.breakevendollar
        if self.target_profit == 0:
            self.targetbepd = 0
            self.targetbepu = 0
        else:
            self.targetbepd = ((self.fixed_cost+self.target_profit) / (self.contrubtion_margin_pct / 100))
            self.targetbepu = (self.fixed_cost+self.target_profit) / self.contrubtion_margin_pct
             
        super().save(*args, **kwargs)



    




