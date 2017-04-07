from rest_framework import serializers
from tourapp.models import Tourpoint


class TourpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourpoint
        fields = ('name', 'longitude', 'latitude', 'category', 'point_type')
