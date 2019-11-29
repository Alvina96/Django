from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('usernamedisplay','phone', 'siteaddress', 'displayeavatar')

    def usernamedisplay(self, obj):
        return User.objects.get(id=obj.user_id).username

    def displayeavatar(self, obj):
        if obj.avatar:
            return u'<img width="100px" height="100px" src="../../../media/%s" />' % (obj.avatar)
    displayeavatar.allow_tags = True
    displayeavatar.short_description = 'Avatar'

admin.site.register(Profile, ProfileAdmin)
