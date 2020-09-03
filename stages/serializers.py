from rest_framework import serializers
from stages.models import Stage, Block, SubStage


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'


class SubStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubStage
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'
