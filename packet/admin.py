from django.contrib import admin
from .models import Packet

class PacketAdmin(admin.ModelAdmin):
    list_display = ('titlename','descriptionname', 'pricename')

    def titlename(self, obj):
        return obj.title
    titlename.short_description = "Название"

    def descriptionname(self, obj):
        return obj.description
    descriptionname.short_description = "Описание"

    def pricename(self, obj):
        return obj.price
    pricename.short_description = "Цена"

admin.site.register(Packet, PacketAdmin)
