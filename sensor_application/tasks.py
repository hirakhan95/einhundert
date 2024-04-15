import time
from datetime import timedelta

from django.conf import settings

from .carbondata import fetch_previous_intensity


def background_task():
    from .models import CarbonIntensityTable
    while True:
        try:
            start_date_time = CarbonIntensityTable.objects.order_by('to_date').last().to_date
            start_date_time = start_date_time + timedelta(minutes=1)
        except:
            start_date_time = settings.START_DATE

        data = fetch_previous_intensity(start_date_time, days_limit=20)

        for d in data:
            obj = CarbonIntensityTable(**d)
            obj.save()

        time.sleep(settings.BACKGROUND_TASK_FREQ)
