from django.contrib import admin

from .models import *


class ItemAdmin(admin.ModelAdmin):
    list_display = ('executor', 'title', 'text')


admin.site.register(Task, ItemAdmin)
admin.site.register(SubTask)
admin.site.register(Category)
admin.site.register(Priority)
admin.site.register(Comment)
admin.site.register(Control)
admin.site.register(Profile)

