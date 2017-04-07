from django.shortcuts import render
from tourapp.models import Tourpoint
from tourapp.serializers import TourpointSerializer
from rest_framework import generics


class TourpointList(generics.ListAPIView):
    queryset = Tourpoint.objects.all()
    serializer_class = TourpointSerializer

class TourpointDetail(generics.RetrieveAPIView):
    queryset = Tourpoint.objects.all()
    serializer_class = TourpointSerializer


