from django.db import models


class Post(models.Model):
   title = models.CharField(max_length = 255)
   description = models.CharField(max_length = 1000)
   bgimage = models.ImageField(upload_to= "post_images", blank=True)
