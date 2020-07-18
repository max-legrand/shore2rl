from django.db import models


class Link(models.Model):
    original_url = models.TextField()
    new_url = models.TextField()
