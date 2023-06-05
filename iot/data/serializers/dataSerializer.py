from rest_framework import serializers
from ..models.scan import Scan


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scan
        fields = ('uuid','time_register')