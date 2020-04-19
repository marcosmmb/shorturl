from django.db import models

from users.models import CustomUser


class Link(models.Model):
    original_url = models.URLField()
    slug = models.CharField(max_length=8)
    counter = models.IntegerField(default=0)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.slug
