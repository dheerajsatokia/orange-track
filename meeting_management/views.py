from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Meeting, Agenda, MOM, MeetingAttendees
from meeting_management import serializer as meeting_serializer


class MeetingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = meeting_serializer.MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.all()


class AgendaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = meeting_serializer.AgendaSerializer

    def get_queryset(self):
        return Agenda.objects.all()


class MOMViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = meeting_serializer.MOMSerializer

    def get_queryset(self):
        return MOM.objects.all()


class MeetingAttendeesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = meeting_serializer.MeetingAttendeesSerializer

    def get_queryset(self):
        return MeetingAttendees.objects.all()
