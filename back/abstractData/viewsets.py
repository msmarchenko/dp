from rest_framework import viewsets
from .models import abstractData
from .serializers import DataSerializer

class DataViewSet(viewsets.ModelViewSet):
    queryset = abstractData.objects.all()
    serializer_class = DataSerializer