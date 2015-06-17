from django.contrib import admin

from . models import FacebookObject, FacebookAnalytics


class FacebookAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('date', 'object', 'page_likes', 'new_likes', 'reach', 'people_engaged')


admin.site.register(FacebookObject)
admin.site.register(FacebookAnalytics, FacebookAnalyticsAdmin)
