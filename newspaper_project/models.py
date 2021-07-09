from django.db import models
from django.db.models.base import Model

# Create your models here.
class Bangladesh(models.Model):
    Title = models.CharField(max_length=300)
    Content = models.TextField()
    content_image = models.ImageField(upload_to='Bangladesh_pic',verbose_name='Uplod Image')
    publish_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        ordering = ('-publish_time', )

    def __str__(self):
        return self.Title

class International(models.Model):
    Title = models.CharField(max_length=300)
    Content = models.TextField()
    content_image = models.ImageField(upload_to='International_pic',verbose_name='Uplod Image')
    publish_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        ordering = ('-publish_time', )

    def __str__(self):
        return self.Title

class Trade(models.Model):
    Title = models.CharField(max_length=300)
    Content = models.TextField()
    content_image = models.ImageField(upload_to='Trade_pic',verbose_name='Uplod Image')
    publish_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        ordering = ('-publish_time', )

    def __str__(self):
        return self.Title

class Entertainment(models.Model):
    Title = models.CharField(max_length=300)
    Content = models.TextField()
    content_image = models.ImageField(upload_to='Entertainment_pic',verbose_name='Uplod Image')
    publish_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        ordering = ('-publish_time', )

    def __str__(self):
        return self.Title

class Sports(models.Model):
    Title = models.CharField(max_length=300)
    Content = models.TextField()
    content_image = models.ImageField(upload_to='Sports_pic',verbose_name='Uplod Image')
    publish_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    class Meta:
        ordering = ('-publish_time', )

    def __str__(self):
        return self.Title