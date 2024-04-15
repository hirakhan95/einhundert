from django.db import models


class CarbonIntensityTable(models.Model):
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    intensity_forecast = models.IntegerField()
    intensity_actual = models.IntegerField()
    intensity_index = models.CharField(max_length=10)

