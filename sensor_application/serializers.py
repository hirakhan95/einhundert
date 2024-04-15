from rest_framework import serializers

from .models import CarbonIntensityTable


class CarbonIntensitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarbonIntensityTable
        fields = ['from_date', 'to_date', 'intensity_forecast', 'intensity_actual', 'intensity_index']
