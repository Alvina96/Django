from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length = 255, blank=False)
    description = models.CharField(max_length = 255)
    image = models.ImageField(upload_to= "topic_images", blank=True)
    precedency = models.IntegerField(default=0)
    level = models.IntegerField(default= 0)
    parent_id = models.IntegerField(default= 0, blank=True)
