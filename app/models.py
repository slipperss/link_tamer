from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    long_url = models.CharField(max_length=255, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    clicks = models.IntegerField(blank=True, default=0)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.long_url
