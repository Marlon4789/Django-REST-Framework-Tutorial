from rest_framework import routers
from .api import ProjectViewSet

# Crear rutas PUT, DELETE, GET, POST

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = router.urls