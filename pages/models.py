from django.db import models

# Create your models here.


class Page(models.Model):
    title=models.CharField(max_length=60)
    permalink=models.CharField(max_length=12,unique=True)
    updatedate=models.DateTimeField(verbose_name="Last Update")
    bodytext = models.TextField("page content",blank=True)

    def __str__(self):
        return self.title