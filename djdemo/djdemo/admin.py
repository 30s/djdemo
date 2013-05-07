from django.contrib import admin

from djdemo.models import *


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial', 'mode', 'remark')


admin.site.register(Device, DeviceAdmin)

