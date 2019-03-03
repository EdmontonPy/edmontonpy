from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from edmontonpy.core.models import Meetup, Sponsor


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def __init__(self, *args, meetup_class=None, sponsor_class=None, **kwargs):
        super().__init__(*args, **kwargs)

        if meetup_class is None:
            meetup_class = Meetup
        self.meetup_class = meetup_class

        if sponsor_class is None:
            sponsor_class = Sponsor
        self.sponsor_class = sponsor_class

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['object'] = None
        try:
            context_data['object'] = self.meetup_class.objects.next_meetup()
        except ObjectDoesNotExist:
            pass
        context_data['sponsors'] = self.sponsor_class.objects.all()
        return context_data
