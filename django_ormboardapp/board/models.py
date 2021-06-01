import datetime

from django.db import models
from django.utils.timezone import now
from django.urls import reverse
# Create your models here.
class Board(models.Model):
    no=models.BigIntegerField(default=1)
    name=models.CharField(max_length=34)  # name VARCHAR(34)
    subject=models.CharField(max_length=1000)
    content=models.TextField()
    pwd=models.CharField(max_length=10)
    regdate=models.DateTimeField(default=now)
    hit=models.BigIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])
    @property
    def update_counter(self):
        self.hit=self.hit+1
        self.save()
    class Meta:
        ordering=['-id']   # id (ASC), -id(DESC)

