from rest_framework import serializers

from .models import Issue, IssueImage, IssueRemark, Notification


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only = ('created_at', 'updated_at', 'raised_by')

    def validate(self, data):
        data['raised_by_id'] = self.context['request'].user.id
        return data


class IssueImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueImage
        fields = '__all__'
        read_only = ('created_at', 'updated_at')


class IssueRemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueRemark
        fields = '__all__'
        read_only = ('created_at', 'updated_at')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


