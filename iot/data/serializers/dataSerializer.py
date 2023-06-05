from rest_framework import serializers
from ..models.scan import Scan


class DataSerializer(serializers.ModelSerializer):
    
    """
    This module defines a serialization model that is used to convert scan data to a 
    format that can be easily transferred over the network using the rest_framework library.

    Attributes: - N/A

    Methods: - DataSerializer: A class that inherits from the ModelSerializer class of the rest_framework library. 
    It defines the fields that will be serialized when an instance of the Scan model is converted to a JSON format,
    such as uuid and time_register.
    """
    class Meta:
        model = Scan
        fields = ('uuid','time_register')