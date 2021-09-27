from django.shortcuts import render
from .models import CalculateBEP
from .forms import BreakEvenPointForm
from django.urls import reverse_lazy,reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib import messages
# Create your views here.

class BEPListView(ListView):
    model = CalculateBEP
    paginate_by = 100
    template_name  = 'bep/bep_list.html'
    
class BEPDetailView(DetailView):
    model = CalculateBEP
    template_name  = 'bep/bep_detail.html'
    

class BEPCreateView(CreateView):
    model = CalculateBEP
    form_class = BreakEvenPointForm
    template_name  = 'bep/bep_form.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Break Even Point Analysis Created Succefully')
        return reverse_lazy('breakevenpoint:bep_list')
        

class BEPUpdateView(UpdateView):
    model = CalculateBEP
    form_class = BreakEvenPointForm
    template_name  = 'bep/bep_form.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Break Even Point Analysis Updated Successfully')
        return reverse('breakevenpoint:bep_detail',kwargs={'pk':self.object.pk})
        

class BEPDeleteView(DeleteView):
    model = CalculateBEP
    template_name  = 'bep/bep_confirm_delete.html'
    extra_context = {'delete_what':'Break Even Point Analysis N°'}
    
    def get_success_url(self):
        messages.success(self.request, 'Break Even Point Analysis Deleted Succefully')
        return reverse_lazy('breakevenpoint:bep_list')