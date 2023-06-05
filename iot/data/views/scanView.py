from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..serializers.dataSerializer import DataSerializer


class ScanView(APIView):
    serializer_class = DataSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors,
                         status=status.HTTP_400_BAD_REQUEST)
