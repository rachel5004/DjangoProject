from django.db import models
from django.urls import reverse
# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=34)
    sex = models.CharField(max_length=4)
    addr = models.TextField()
    tel = models.TextField()
    def __str__(self):
        return self.name+"("+self.sex+")"
    def get_absolute_url(self):
        return reverse('detail/',args=[str(self.id)])