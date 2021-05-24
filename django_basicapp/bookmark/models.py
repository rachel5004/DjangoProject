from django.db import models
'''
Binary	models.BinaryField()
Boolean	models.BooleanField()
Boolean	models.NullBooleanField()
Date/time	models.DateField()
Date/time	models.TimeField()
Date/time	models.DateTimeField()
Date/time	models.DurationField()
Number	models.AutoField()  => 정수
Number	models.BigIntegerField() => long
Number	models.DecimalField(max_digits=X,decimal_places=Y)
Number	models.FloatField() => 실수
Number	models.IntegerField()
Number	models.PositiveIntegerField()
Number	models.PositiveSmallIntegerField()
Number	options.SmallIntegerField()
Text	models.CharField(max_length=N) => varchar2
Text	models.TextField() => CLOB
Text (Specialized)	models.CommaSeparatedIntegerField(max_length=50)
Text (이메일)	models.EmailField()
Text (파일)	models.FileField()
Text (Specialized)	models.FilePathField()
Text (Specialized)	models.ImageField()
Text (이미지)	models.GenericIPAddressField()
Text (Specialized)	models.SlugField()
Text (Specialized)	models.URLField()
Text (Specialized)	models.UUIDField()
'''
# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')
    def __str__(self):
        return "name: "+self.site_name+" ,URL: "+self.url