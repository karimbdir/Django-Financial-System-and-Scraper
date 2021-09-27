from .models import CalculateBEP
from django import forms



class BreakEvenPointForm(forms.ModelForm):
    class Meta:
        model = CalculateBEP
        fields = ['project_title','sales','units_sold','variable_cost','contribution_margin',
        'contrubtion_margin_pct','fixed_cost','target_profit']
        