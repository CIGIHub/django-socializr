from django.contrib import admin

from . models import YouTubeChannel, YouTubeAnalytics


class YouTubeAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('date', 'channel', 'views', 'subscribers', 'video_count')


admin.site.register(YouTubeChannel)
admin.site.register(YouTubeAnalytics, YouTubeAnalyticsAdmin)
