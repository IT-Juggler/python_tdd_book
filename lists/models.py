"""docstring"""
from django.db import models
from django.core.urlresolvers import reverse

class List(models.Model):
    """docstring"""

    def get_absolute_url(self):
        """docstring"""
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    """docstring"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
