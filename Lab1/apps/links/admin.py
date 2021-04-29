from django.contrib import admin
from .models import Link, UserLike


class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


admin.site.register(Link)
admin.site.register(UserLike)