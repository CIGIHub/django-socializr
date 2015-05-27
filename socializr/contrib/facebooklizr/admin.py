from django.contrib import admin

from . models import FacebookObject, FacebookAnalytics

admin.site.register(FacebookObject)
admin.site.register(FacebookAnalytics)
