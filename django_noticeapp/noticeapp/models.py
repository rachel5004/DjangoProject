from django.db import models

# Create your models here.
class Noticeapp(models.Model):
    name=models.CharField(max_length=34)
    subject=models.CharField(max_length=500)
    content=models.TextField()
    regdate=models.DateTimeField()
    hit=models.FloatField()
