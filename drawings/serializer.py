from rest_framework import serializers
from drawings.models import Plans, PlanOption, DrawingRemark, Drawing


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'


class PlanOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanOption
        fields = '__all__'


class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'uploaded_by')

    def validate(self, data):
        data['uploaded_by_id'] = self.context['request'].user.id
        return data


class DrawingRemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrawingRemark
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'remarked_by')

    def validate(self, data):
        data['remarked_by_id'] = self.context['request'].user.id
        return data
