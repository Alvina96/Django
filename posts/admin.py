from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptionname','bgimage')

    def titlename(self, obj):
        return obj.title
    titlename.short_description = "Название"

    def descriptionname(self, obj):
        return obj.description
    descriptionname.short_description = "Описание"

admin.site.register(Post, PostAdmin)
