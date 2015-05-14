from django.db import models

from socializr.models import PerDayAnalyticsBase

class YouTubeChannel(models.Model):
    channel_id = models.CharField(max_length=256)


class YouTubeAnalytics(PerDayAnalyticsBase):
    channel = models.ForeignKey(YouTubeChannel)

    # ever increasing
    views = models.PositiveIntegerField(default=0)
    subscribers = models.PositiveIntegerField(default=0)
    video_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'youtube analytics'


