from rest_framework import serializers

from config.settings import HOST, PORT
from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    shortened_url = serializers.SerializerMethodField()  # Поле для вывода полного урла после укорочачивания

    class Meta:
        model = Link
        fields = ('id', 'long_url', 'owner', 'clicks', 'created_date', 'shortened_url')
        read_only_fields = ('id', 'owner', 'clicks', 'created_date', 'shortened_url')

    def get_shortened_url(self, obj):
        return f'{HOST}:{PORT}/api/r/{obj.id}/'

    def to_representation(self, instance):
        # Вывод информации о количестве кликов только владельцу ссылки либо админу
        result = super().to_representation(instance)
        request_user = self.context['request'].user
        if request_user.id == result['owner'] or request_user.is_staff:
            return result
        result.pop('clicks')
        return result
