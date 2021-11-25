"""docstring"""
from django.db import models

class List(models.Model):
    """docstring"""
    pass


class Item(models.Model):
    """docstring"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
