from django.contrib.auth.models import User
from django.urls import reverse

from django.db import models

# Create your models here.


class Paste(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag', related_name='tag')
    text_type = models.ForeignKey('TextType', on_delete=models.PROTECT, null=True, blank=True)
    expiration_date = models.DateField(blank=True, null=True)
    access_password = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('paste', args=[str(self.pk)])
        # return reverse('paste', kwargs={'paste_id': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class TextType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

