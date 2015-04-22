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
    # https://graph.facebook.com/v2.3/<page_id>/[likes]
    page_likes = models.PositiveIntegerField(default=0)

    # incremental
    #https://graph.facebook.com/v2.3/100911698621/insights/page_fan_adds_unique
    new_likes = models.PositiveIntegerField(default=0)
    # https://graph.facebook.com/v2.3/<page_id>/insights/page_posts_impressions
    reach = models.PositiveIntegerField(default=0)
    # https://graph.facebook.com/v2.3/<page_id>/insights/page_engaged_users/day
    people_engaged = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'facebook analytics'

