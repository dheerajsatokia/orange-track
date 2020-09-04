from rest_framework import serializers
from tasks.models import Tasks, TaskRemarks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by')

    def validate(self, data):
        data['created_by_id'] = self.context['request'].user.id
        return data


class TaskRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskRemarks
        field = '__all__'
        read_only_fields = ('created_at', 'updated_at')
