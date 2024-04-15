from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarbonIntensityTable
from .serializers import CarbonIntensitySerializer


class DateRangeView(APIView):
    def get(self, request):
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        if from_date and to_date:
            entries = CarbonIntensityTable.objects.filter(from_date__gte=from_date, to_date__lte=to_date)
            serializer = CarbonIntensitySerializer(entries, many=True)
            return Response(serializer.data)
        return Response({"error": "Both from_date and to_date parameters are required."},
                        status=status.HTTP_400_BAD_REQUEST)


class IndexTypeView(APIView):
    def get(self, request):
        index = request.query_params.get('index')
        if index:
            entries = CarbonIntensityTable.objects.filter(intensity_index=index)
            serializer = CarbonIntensitySerializer(entries, many=True)
            return Response(serializer.data)
        return Response({"error": "index parameter is required."}, status=status.HTTP_400_BAD_REQUEST)


class ActualRangeView(APIView):
    def get(self, request):
        min_actual = request.query_params.get('min_actual')
        max_actual = request.query_params.get('max_actual')
        if min_actual and max_actual:
            entries = CarbonIntensityTable.objects.filter(intensity_actual__gte=min_actual,
                                                          intensity_actual__lte=max_actual)
            serializer = CarbonIntensitySerializer(entries, many=True)
            return Response(serializer.data)
        return Response({"error": "Both min_actual and max_actual parameters are required."},
                        status=status.HTTP_400_BAD_REQUEST)


class CarbonIntensityFilterView(APIView):
    def get(self, request):
        # Retrieve query parameters
        from_date = request.query_params.get('from_date')
        to_date = request.query_params.get('to_date')
        min_value = request.query_params.get('min_value')
        max_value = request.query_params.get('max_value')
        min_forecast = request.query_params.get('min_forecast')
        max_forecast = request.query_params.get('max_forecast')
        intensity_index = request.query_params.get('intensity_index')

        # Build the query incrementally
        queries = Q()
        if from_date:
            queries &= Q(from_date__gte=from_date)
        if to_date:
            queries &= Q(to_date__lte=to_date)

        if min_value:
            queries &= Q(intensity_actual__gte=min_value)

        if max_value:
            queries &= Q(intensity_actual__lte=max_value)

        if min_forecast:
            queries &= Q(intensity_forecast__gte=min_forecast)

        if max_forecast:
            queries &= Q(intensity_forecast__lte=max_forecast)

        if intensity_index:
            queries &= Q(intensity_index=intensity_index)

        # Execute the query
        entries = CarbonIntensityTable.objects.filter(queries)
        serializer = CarbonIntensitySerializer(entries, many=True)
        return Response(serializer.data)
