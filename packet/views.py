from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from posts.models import Post
from packet.models import Packet
from home.models import Profile

def packetview(request):

    post = Post.objects.get(pk=2)
    packet = Packet.objects.all()
    profileroot = Profile.objects.get(user_id=1)

    args = {'post':post, 'packets':packet, 'profileroot':profileroot}
    return render(request, 'packet/home.html',args)
