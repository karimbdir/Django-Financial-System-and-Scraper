from django.core.mail import send_mail
from django.views.generic import FormView

from transactions.forms.feedback import BugReportForm, RequestNewFeatureForm
from transactions.settings import transactions_FEEDBACK_EMAIL_LIST, transactions_FEEDBACK_FROM_EMAIL
from transactions.views.mixins import LoginRequiredMixIn, SuccessUrlNextMixIn


class BugReportView(LoginRequiredMixIn,
                    SuccessUrlNextMixIn,
                    FormView):
    http_method_names = ['post']
    form_class = BugReportForm

    def form_valid(self, form):
        form_data = form.cleaned_data
        message = f'How to reproduce?: {form_data["reproduce"]}\n' + \
                  f'Expectation: {form_data["expectation"]}\n' + \
                  f'Device: {form_data["device"]}\n' + \
                  f'From user: {self.request.user.username}\n' + \
                  f'User email: {self.request.user.email}'
        if transactions_FEEDBACK_EMAIL_LIST:
            send_mail(
                subject=f'DJL Bug Report',
                from_email=transactions_FEEDBACK_FROM_EMAIL,
                recipient_list=transactions_FEEDBACK_EMAIL_LIST,
                fail_silently=True,
                message=message)
        return super().form_valid(form)


class RequestNewFeatureView(LoginRequiredMixIn,
                            SuccessUrlNextMixIn,
                            FormView):
    http_method_names = ['post']
    form_class = RequestNewFeatureForm

    def form_valid(self, form):
        form_data = form.cleaned_data
        message = f'Description: {form_data["feature_description"]}\n' + \
                  f'Solution: {form_data["solution"]}\n' + \
                  f'Alternatives: {form_data["alternatives"]}\n' + \
                  f'From user: {self.request.user.username}\n' + \
                  f'User email: {self.request.user.email}'
        if transactions_FEEDBACK_EMAIL_LIST:
            send_mail(
                subject=f'DJL New Feature Request',
                from_email=transactions_FEEDBACK_FROM_EMAIL,
                recipient_list=transactions_FEEDBACK_EMAIL_LIST,
                fail_silently=True,
                message=message)
        return super().form_valid(form)
