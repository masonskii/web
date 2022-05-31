from django.contrib.auth.base_user import BaseUserManager
from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(auto_now=True, null=True, blank=True)
    author = models.CharField(max_length=99, null=False, blank=False)
    type = models.CharField(max_length=99)
    category = models.CharField(max_length=99)
    count_like = models.IntegerField(default=0)
    img = models.ImageField(upload_to='files/image/news_img/%Y-%m-%d/')
    content = models.CharField(max_length=999, null=True, blank=True)
    is_actual = models.BooleanField(default=True)
