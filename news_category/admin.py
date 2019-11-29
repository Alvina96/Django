from django.contrib import admin
from .models import NewsCategory

class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('titlename',)

    def titlename(self, obj):
        return obj.title
    titlename.short_description = "Название"

admin.site.register(NewsCategory, NewsCategoryAdmin)
