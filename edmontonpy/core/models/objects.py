import pytz

from .dals import MeetupDAL, PresentationDAL, PresenterDAL, SponsorDAL

America_Edmonton = pytz.timezone('America/Edmonton')

class Meetup(MeetupDAL):
    @property
    def is_virtual(self):
        return self.url != ''

    def __str__(self):
        return f'{self.date_time.astimezone(America_Edmonton)}'


class Presentation(PresentationDAL):
    def __str__(self):
        return f'{self.name} - {self.presenter}'


class Presenter(PresenterDAL):
    @property
    def full_name(self):
        return str.strip(f'{self.first_name} {self.last_name}')

    def __str__(self):
        return self.full_name


class Sponsor(SponsorDAL):
    def __str__(self):
        return f'{self.name}'
