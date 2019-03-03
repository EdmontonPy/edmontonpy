from django.urls import path
from django.views.generic import TemplateView

from .views import IndexTemplateView

urlpatterns = [
    path(
        '',
        IndexTemplateView.as_view(),
        name='home'
    ),
    path(
        'code-of-conduct',
        TemplateView.as_view(template_name='code-of-conduct.html'),
        name='code-of-conduct'
    ),
    path(
        'privacy-policy',
        TemplateView.as_view(template_name='privacy-policy.html'),
        name='privacy-policy'
    ),
    path(
        'terms-and-conditions',
        TemplateView.as_view(template_name='terms-and-conditions.html'),
        name='terms-and-conditions'
    ),
]
