from rest_framework import serializers

from .models import Meeting, Agenda, MOM, MeetingAttendees


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'organizer')

    def validate(self, data):
        data['organizer_id'] = self.context['request'].user.id
        return data


class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class MOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = MOM
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class MeetingAttendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingAttendees
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')



