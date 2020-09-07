from rest_framework import serializers

from inventory.models import InventoryItem, Vendor, PurchaseRecord, VendorVisit


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only = ('created_at', 'updated_at')


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class PurchaseRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRecord
        fields = '__all__'
        read_only = ('created_at', 'updated_at')


class VendorVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorVisit
        fields = '__all__'
        read_only = ('created_at', 'updated_at')

    def validate(self, data):
        data['updated_by_id'] = self.context['request'].user.id
        return data


