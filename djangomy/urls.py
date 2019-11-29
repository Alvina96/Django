"""djangomy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout

from home.views import redirecthome, cabinet, loginuser, confirmuser, registrationuser
from news.views import newsview
from packet.views import packetview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', redirecthome),
    url(r'^packets/', packetview),
    url(r'^cabinet/', cabinet),
    url(r'^news/', newsview),
    url(r'^login/', loginuser),
    url(r'^registration/', registrationuser),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^confirm/(?P<user>\w+)/$', confirmuser),
     url(
        r'^logout/',
        logout,kwargs={'next_page': '/'}
    ),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
