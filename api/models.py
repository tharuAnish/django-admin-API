from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.base import Model
# Create your models here.

class Services(models.Model):
    s_name=models.CharField(max_length=400)
    s_desc=RichTextField()
    s_pic = models.ImageField(upload_to='media/serviceimage', null=True)
    is_active=models.BooleanField(default=True)
    s_rank=models.IntegerField(default=0)
    def __str__(self):
        return self.s_name
