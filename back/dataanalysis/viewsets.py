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

class CalculateViewset(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def calc(self, request):
        data = request.data
        if data['algos'] == 'Linear Reg':
            ret = Calculations.LinearReg(data['params'])
            return Response(ret)
        return Response(request.data)