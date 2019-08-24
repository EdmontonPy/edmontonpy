import pytz
from django.db import migrations

def fix_times(apps, schema_editor):
    """
    Change any meetups at 23:59 UTC in the DB to be at the correct time in
    Edmonton time, and save back as UTC.
    """
    Meetup = apps.get_model("core", "Meetup")
    America_Edmonton = pytz.timezone('America/Edmonton')

    bad_dates = Meetup.objects.filter(date_time__hour=23, date_time__minute=59)
    for meetup in bad_dates:
        date_time = meetup.date_time

        # Make unaware
        date_time = date_time.replace(tzinfo=None)

        date_time = date_time.replace(hour=18, minute=30)
        date_time = America_Edmonton.localize(date_time)
        meetup.date_time = date_time

        meetup.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fix_times)
    ]
