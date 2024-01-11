from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

# Crear API
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny] # Cualquiera tiene acceso a la api.
    serializer_class = ProjectSerializer