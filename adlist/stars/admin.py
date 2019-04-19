from django.contrib import admin

from stars.models import Star, Comment

# Register your models here.

admin.site.register(Star)
admin.site.register(Comment)