from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from socializr.models import PerDayAnalyticsBase


@python_2_unicode_compatible
class YouTubeChannel(models.Model):
    name = models.CharField(max_length=256)
    channel_id = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class YouTubeAnalytics(PerDayAnalyticsBase):
    channel = models.ForeignKey(YouTubeChannel)

    # ever increasing
    views = models.PositiveIntegerField(default=0)
    subscribers = models.PositiveIntegerField(default=0)
    video_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'youtube analytics'


