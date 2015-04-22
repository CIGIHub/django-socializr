from django.db import models

from socializr.models import PerDayAnalyticsBase

class FacebookObject(models.Model):
    '''
    Currently only Pages are tested
    '''
    object_id = models.CharField(max_length=256)


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

