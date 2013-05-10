from django.contrib import admin

from djdemo.models import *


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial', 'mode', 'remark')


class DictKeyAdmin(admin.ModelAdmin):
    list_display = ('name', )


class DictValueAdmin(admin.ModelAdmin): 
    list_display = ('key', 'value')


admin.site.register(Device, DeviceAdmin)
admin.site.register(DictKey, DictKeyAdmin)
admin.site.register(DictValue, DictValueAdmin)
