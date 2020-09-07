from rest_framework import serializers
from stages.models import Stage, Block, SubStage,Level


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class SubStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubStage
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

