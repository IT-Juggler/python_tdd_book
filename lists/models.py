"""docstring"""
from django.db import models


class Item(models.Model):
    """docstring"""
    text = models.TextField(default='')
