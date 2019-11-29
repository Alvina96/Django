from django.db import models

class Packet(models.Model):
   title = models.CharField(max_length = 255)
   description = models.CharField(max_length = 255)
   price = models.CharField(max_length = 255)
   classname = models.CharField(max_length = 255)
