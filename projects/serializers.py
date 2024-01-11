from rest_framework import serializers
from .models import Project

# Unserialiser convierte los modelos a diccionarios en formato python para ser convertidos en datos JSON.

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'create_date')
        read_only_fields = ('create_date',) # Este campo no se puede editar, solo lectura.