from __future__ import unicode_literals

from django.db import models


# Register your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Gist(models.Model):
    name = models.CharField(max_length=100000)
    url = models.CharField(max_length=100000)

    def __str__(self):
        return self.url


class Pattern(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100000)
    features = models.CharField(max_length=100000)
    implementation = models.CharField(max_length=100000)
    uml = models.CharField(max_length=100000)
    gists = models.ForeignKey(Gist)
    output = models.CharField(max_length=100000)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
