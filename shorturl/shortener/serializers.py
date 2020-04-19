from rest_framework import serializers

from .models import Link
from .utils import generate_slug


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ("slug", "original_url")
        read_only_fields = ("slug",)

    def create(self, validated_data):
        link_data = {
            "original_url": validated_data["original_url"],
            "slug": generate_slug(),
            "creator": self.context.get("request").user,
        }
        instance = super().create(link_data)
        return instance
