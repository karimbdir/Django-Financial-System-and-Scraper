from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView

from transactions.forms.vendor import VendorModelForm
from transactions.models.entity import EntityModel
from transactions.models.vendor import VendorModel
from transactions.views.mixins import LoginRequiredMixIn


class VendorModelListView(LoginRequiredMixIn, ListView):
    template_name = 'transactions/vendor_list.html'
    context_object_name = 'vendors'
    PAGE_TITLE = _('Vendor List')
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return VendorModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        ).order_by('-updated')


class VendorModelCreateView(LoginRequiredMixIn, CreateView):
    template_name = 'transactions/vendor_create.html'
    PAGE_TITLE = _('Create New Vendor')
    form_class = VendorModelForm
    context_object_name = 'vendor'
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }

    def get_queryset(self):
        return VendorModelForm.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('transactions:vendor-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        customer_model: VendorModel = form.save(commit=False)
        entity_model = EntityModel.objects.for_user(
            user_model=self.request.user
        ).get(slug__exact=self.kwargs['entity_slug'])
        customer_model.entity = entity_model
        customer_model.save()
        return super().form_valid(form)


class VendorModelUpdateView(LoginRequiredMixIn, UpdateView):
    template_name = 'transactions/vendor_update.html'
    PAGE_TITLE = _('Vendor Update')
    context_object_name = 'vendor'
    form_class = VendorModelForm
    extra_context = {
        'page_title': PAGE_TITLE,
        'header_title': PAGE_TITLE,
        'header_subtitle_icon': 'bi:person-lines-fill'
    }
    slug_url_kwarg = 'vendor_pk'
    slug_field = 'uuid'

    def get_queryset(self):
        return VendorModel.objects.for_entity(
            entity_slug=self.kwargs['entity_slug'],
            user_model=self.request.user
        )

    def get_success_url(self):
        return reverse('transactions:vendor-list',
                       kwargs={
                           'entity_slug': self.kwargs['entity_slug']
                       })

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)