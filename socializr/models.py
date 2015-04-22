from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class PerDayAnalyticsBase(models.Model):
    date = models.DateField()

    class Meta:
        abstract = True
        ordering = ('-date',)
