from django.contrib import admin

from .models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ('titlename', 'descriptionname','image')

    def titlename(self, obj):
        return obj.title
    titlename.short_description = "Название"

    def descriptionname(self, obj):
        return obj.description
    descriptionname.short_description = "Описание"

admin.site.register(Topic, TopicAdmin)
