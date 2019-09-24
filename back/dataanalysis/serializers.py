from rest_framework import serializers
from .models import Composition
from .models import Parameter
from .models import Machine
from .models import Order
from .models import Measurements

class CompositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = '__all__'

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class MeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurements
        fields = '__all__'
