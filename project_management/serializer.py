from rest_framework import serializers

from project_management.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only = ('created_at', 'updated_at')

