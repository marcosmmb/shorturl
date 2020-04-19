from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from shortener.serializers import ShortUrlSerializer


class CreateShortUrl(CreateAPIView):
    serializer_class = ShortUrlSerializer
    permission_classes = (IsAuthenticated,)
