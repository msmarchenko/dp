from rest_framework import routers
from abstractData.viewsets import DataViewSet

from dataanalysis.viewsets import CompositionViewSet
from dataanalysis.viewsets import ParameterViewSet
from dataanalysis.viewsets import MachineSerializerViewSet
from dataanalysis.viewsets import OrderSerializerViewSet
from dataanalysis.viewsets import MeasurementsViewSet
from dataanalysis.viewsets import CalculateViewSet
from dataanalysis.viewsets import EbemViewSet

#from dataanalysis.views import aboutview

router = routers.DefaultRouter()
router.register(r'data', DataViewSet)

router.register(r'composition', CompositionViewSet)
router.register(r'parameter', ParameterViewSet)
router.register(r'machine', MachineSerializerViewSet)
router.register(r'order', OrderSerializerViewSet)
router.register(r'measurements', MeasurementsViewSet)
router.register(r'calc', CalculateViewSet, basename='calc')
#router.register(r'ebemvrot', EbemViewSet, basename='ebem')
#router.register(r'ebemvrot', aboutview,basename='aboutview')
