from rest_framework import serializers
from staff.models import StaffCategory, StaffAttendance, StaffSubType


class StaffCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffCategory
        fields = '__all__'


class StaffSubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffSubType
        fields = '__all__'


class StaffAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAttendance
        fields = '__all__'
        read_only_field = ('created_at', 'updated_at', 'updated_by')

    def validate(self, data):
        data['updated_by_id'] = self.context['request'].user.id
        return data
