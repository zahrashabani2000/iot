from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers.dataSerializer import DataSerializer


class ScanView(APIView):
    
    """Handle POST requests to create a new Scan object.

    This view defines a post() method that expects a data payload containing
    information about a new Scan object to be created. The data is validated
    using the DataSerializer class. If the data is valid, it is saved using
    the serializer's save() method. If not, an error response is returned.

    Attributes:
        serializer_class: The serializer class to use to validate and
            deserialize the data payload.

    Methods:
        post(request): Create a new Scan object with the provided data.

    Returns:
        A Response object with the serialized data and the appropriate HTTP
        status code (201 if successful or 400 if validation errors occurred).
    """
    
    serializer_class = DataSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                         status=status.HTTP_400_BAD_REQUEST)
