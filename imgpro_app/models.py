from django.db import models
import os

# Create your models here.

class TBImage(models.Model):
    slideNumber = models.CharField(max_length=60)
    def_path = "img/"+str(slideNumber)+"/default/"
    pro_path = "img/"+str(slideNumber)+"/processed/"
    imgDefault = models.ImageField(upload_to=def_path,null=True, blank=True)
    imgProcessed = models.ImageField(upload_to=pro_path,null=True, blank=True)