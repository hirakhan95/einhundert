from django.urls import path

from .views import DateRangeView, IndexTypeView, ActualRangeView, CarbonIntensityFilterView

urlpatterns = [
    path('api/carbon_intensity/date_range/', DateRangeView.as_view(), name='date_range'),
    path('api/carbon_intensity/index_type/', IndexTypeView.as_view(), name='index_type'),
    path('api/carbon_intensity/actual_range/', ActualRangeView.as_view(), name='actual_range'),
    path('api/carbon_intensity/', CarbonIntensityFilterView.as_view(), name='carbon_intensity_filter'),
]
