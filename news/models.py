from django.db import models

class News(models.Model):
   title = models.CharField(max_length = 255)
   description = models.CharField(max_length = 255)
   category = models.IntegerField(default=0)
   status = models.IntegerField(default= 0)
   created_at = models.DateTimeField(max_length = 255)
   updated_at = models.DateTimeField(max_length = 255)
   precedency = models.IntegerField(default= 0)

def __str__(self):
        return self.name
