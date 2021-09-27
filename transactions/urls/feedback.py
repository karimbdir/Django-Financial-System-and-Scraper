from django.urls import path
from transactions.views import feedback

urlpatterns = [
    path('bug-report/', feedback.BugReportView.as_view(), name='bug-report'),
    path('new-feature/', feedback.RequestNewFeatureView.as_view(), name='new-feature')
]
