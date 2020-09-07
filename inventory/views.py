from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from inventory.models import InventoryItem, Vendor, PurchaseRecord, VendorVisit
from inventory import serializer as inventory_serializer


class InventoryItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = inventory_serializer.InventoryItemSerializer

    def get_queryset(self):
        return InventoryItem.objects.all()


class VendorViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = inventory_serializer.VendorSerializer

    def get_queryset(self):
        return Vendor.objects.all()


class PurchaseRecordViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = inventory_serializer.PurchaseRecordSerializer

    def get_queryset(self):
        return PurchaseRecord.objects.all()


class VendorVisitViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = inventory_serializer.VendorVisitSerializer

    def get_queryset(self):
        return VendorVisit.objects.all()
