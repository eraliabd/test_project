from rest_framework import serializers
from .models import Language


class LanguageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)

    def get_image_url(self, obj):
        return obj.picture

    class Meta:
        model = Language
        fields = ['title', 'photo', 'image_url']
        read_only_fields = ['id', 'image_url']
