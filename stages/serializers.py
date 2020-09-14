from rest_framework import serializers

from stages.models import Stage, Block, SubStage, Level, ProgressInventoryEntry, ProgressEntry, \
    ProgressComment, ProgressEntryMedia


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


class ProgressInventoryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressInventoryEntry
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ProgressCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressComment
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ProgressEntryMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressEntryMedia
        fields = '__all__'


class ProgressEntrySerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    inventory_entries = serializers.SerializerMethodField()
    media = serializers.SerializerMethodField()

    class Meta:
        model = ProgressEntry
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'is_approved')

    def get_comments(self, progress_entry):
        return [ProgressComment(comment).data for comment in
                ProgressComment.objects.filter(progress_entry=progress_entry)]

    def get_inventory_entries(self, progress_entry):
        return [ProgressInventoryEntrySerializer(inventory_entry).data for inventory_entry in
                ProgressInventoryEntry.objects.filter(progress_entry=progress_entry)]

    def get_media(self, progress_entry):
        return [ProgressEntryMediaSerializer(media).data for media in
                ProgressEntryMedia.objects.filter(progress_entry=progress_entry)]
