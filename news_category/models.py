from django.db import models

class NewsCategory(models.Model):
   title = models.CharField(max_length = 255)
