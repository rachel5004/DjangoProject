from django.db import models
'''
    CREATE TABLE notice()
    ORM
'''
# Create your models here.
class Notice(models.Model):
    name = models.CharField(max_length=34)
    subject = models.CharField(max_length=500)
    content = models.TextField()
    regdate = models.DateTimeField()