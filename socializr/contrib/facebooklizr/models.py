from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from socializr.models import PerDayAnalyticsBase


@python_2_unicode_compatible
class FacebookObject(models.Model):
    """
    Currently only Pages are tested
    """
    name = models.CharField(max_length=256)
    object_id = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class FacebookAnalytics(PerDayAnalyticsBase):
    object = models.ForeignKey(FacebookObject)
    # ever increasing
    page_likes = models.PositiveIntegerField(default=0)

    # incremental
    new_likes = models.PositiveIntegerField(default=0)
    reach = models.PositiveIntegerField(default=0)
    people_engaged = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'facebook analytics'

