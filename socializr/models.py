from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class PerDayAnalyticsBase(models.Model):
    user_id = models.CharField(max_length=256)
    date = models.DateField()

    class Meta:
        abstract = True

