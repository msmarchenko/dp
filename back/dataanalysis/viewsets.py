from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Composition
from .serializers import CompositionSerializer

from .models import Parameter
from .serializers import ParameterSerializer

from .models import Machine
from .serializers import MachineSerializer

from .models import Order
from .serializers import OrderSerializer

from .models import Measurements
from .serializers import MeasurementsSerializer
#странная конструкция ._.
from .Calculations import Calculations

import json

class CompositionViewSet(viewsets.ModelViewSet):
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer

class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer

class MachineSerializerViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class OrderSerializerViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class MeasurementsViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer

class CalculateViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def calc(self, request):
        data = request.data
        if data['algos'] == 'Umap':
            ret = Calculations.CalcUmap(data['params'])
            return Response(ret)
        if data['algos'] == 'CNN':
            ret = Calculations.CalcCNN(data['params'])
            return Response(ret)
        if data['algos'] == "Random Forest":
            ret = Calculations.LinearReg(data['params'])
            return Response(ret)
        if data['algos'] == "Hist":
            ret = Calculations.Hist(data['machine'])
            return Response(ret)
        return Response(request.data)

class EbemViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementsSerializer
    @action(detail=False, methods=['get'])
    def ebem(self, request):
        print("ebemvrot")
        data = request.data
        return Response(request.data)
