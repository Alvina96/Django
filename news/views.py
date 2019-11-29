from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from news.models import News
from news_category.models import NewsCategory
from django.core.mail import send_mail
from home.models import Profile



def newsview(request):
    news1 = News.objects.all().filter(category=1)
    news2 = News.objects.all().filter(category=2)
    news3 = News.objects.all().filter(category=3)
    
    category = NewsCategory.objects.all()
    profileroot = Profile.objects.get(user_id=1)

    args = {'news1':news1,'news2':news2,'news3':news3, 'newscat':category, 'profileroot':profileroot}
    return render(request, 'news/home.html',args)
