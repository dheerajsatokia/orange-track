from rest_framework import serializers
from site_manage.models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = '__all__'
        read_only_field = ('created_at', 'updated_at')
