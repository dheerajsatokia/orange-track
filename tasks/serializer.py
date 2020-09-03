from rest_framework import serializers
from tasks.models import Tasks, TaskRemarks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'


class TaskRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRemarks
        field = '__all__'
