from django.db import models

from socializr.models import AnalyticsBase


class FacebookAnalytics(PerDayAnalyticsBase):
    # ever increasing
    page_likes = models.PositiveIntegerField()

    # incremental
    new_likes = models.PositiveIntegerField()
    reach = models.PositiveIntegerField()
    people_engaged = models.PositiveIntegerField

