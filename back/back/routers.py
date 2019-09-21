from rest_framework import routers
from abstractData.viewsets import DataViewSet
router = routers.DefaultRouter()
router.register(r'data', DataViewSet)