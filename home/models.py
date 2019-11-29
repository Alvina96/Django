from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    email = forms.EmailField(max_length=254, help_text='',widget=forms.TextInput(attrs={'placeholder': 'Введите E-mail'}))
    password2 = forms.CharField(max_length=254, help_text='',widget=forms.TextInput(attrs={'placeholder': 'Введите Пароль'}))

    def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields.pop('password2')
    class Meta:
        model = User
        fields = ('username','email', 'password2', )
        # help_texts = {
        #     'username': '',
        # }
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, blank=True)
    siteaddress = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='profile_images', blank=True)
    fb = models.CharField(max_length=255, blank=True)
    vk = models.CharField(max_length=255, blank=True)
    tw = models.CharField(max_length=255, blank=True)
    ts = models.CharField(max_length=255, blank=True)
    watsapp = models.CharField(max_length=255, blank=True)
    description = models.TextField(max_length=1000, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()
