from rest_framework import serializers


from data import models


class Data_serializer(serializers.ModelSerializer):
    """Serializers the objects of Scan model"""
    class Meta:
        model = models.Scan
        fields = ('uuid','time_register')