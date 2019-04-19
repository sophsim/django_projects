from django.contrib import admin

from cats.models import Cat, Comment

# Register your models here.

admin.site.register(Cat)
admin.site.register(Comment)