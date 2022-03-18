from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200, blank=False)
    isbn = models.CharField(max_length=200, blank=False)
    publisher = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.title

