from django.db import models

class projects(models.Model):
  link = models.CharField(max_length=255)
  image_property = models.FileField(upload_to='img',max_length=255,null=True,blank=True,default=None)
  catagory = models.CharField(max_length=255,null=True,blank=True)
  name=models.CharField(max_length=255,null=True,blank=True)
  description = models.CharField(max_length=255,null=True,blank=True)
  name=models.CharField(max_length=255,null=True,blank=True)


  # Sonira777&