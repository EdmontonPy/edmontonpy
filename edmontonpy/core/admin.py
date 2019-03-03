from django.contrib import admin

from .models import Meetup, Presentation, Presenter, Sponsor

admin.site.register(Meetup)
admin.site.register(Presentation)
admin.site.register(Presenter)
admin.site.register(Sponsor)
