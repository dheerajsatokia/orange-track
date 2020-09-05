from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Issue, IssueImage, IssueRemark, Notification
from issue import serializer as issue_serializer


class IssueViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = issue_serializer.IssueSerializer

    def get_queryset(self):
        return Issue.objects.all()


class IssueImageViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = issue_serializer.IssueImageSerializer


class IssueRemarkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = issue_serializer.IssueRemarkSerializer

    def get_queryset(self):
        return IssueRemark.objects.all()


class NotificationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = issue_serializer.NotificationSerializer

    def get_queryset(self):
        return Notification.objects.all()
