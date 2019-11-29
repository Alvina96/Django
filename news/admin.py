from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('category','title', 'descriptionname', 'created_at', 'updated_at', 'status', 'precedency')

    def titlename(self, obj):
        return obj.title
    titlename.short_description = "Название"

    def descriptionname(self, obj):
        return obj.description
    descriptionname.short_description = "Описание"

admin.site.register(News, NewsAdmin)
