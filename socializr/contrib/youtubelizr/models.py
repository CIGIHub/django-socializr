from django.db import models

from socializr.models import PerDayAnalyticsBase

class YouTubeChannel(models.Model):
    '''
    Currently only Pages are tested
    '''
    channel_id = models.CharField(max_length=256)


class YouTubeAnalytics(PerDayAnalyticsBase):
    channel = models.ForeignKey(YouTubeChannel)
    
    # ever increasing
    # https://graph.facebook.com/v2.3/<page_id>/[likes]
    subscribers = models.PositiveIntegerField(default=0)
    videos = models.PositiveIntegerField(default=0)

    # incremental
    # See https://developers.google.com/apis-explorer/#p/youtubeAnalytics/v1/youtubeAnalytics.reports.query?ids=channel%253D%253DMINE&start-date=2014-05-01&end-date=2014-06-30&metrics=views%252Ccomments%252CfavoritesAdded%252Clikes%252Cdislikes%252CestimatedMinutesWatched%252CaverageViewDuration&_h=2&
    # GET https://www.googleapis.com/youtube/analytics/v1/reports?ids=channel%3D%3DMINE&start-date=2014-05-01&end-date=2014-06-30&metrics=views%2Ccomments%2CfavoritesAdded%2Clikes%2Cdislikes%2CestimatedMinutesWatched%2CaverageViewDuration&key={YOUR_API_KEY}
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'youtube analytics'

