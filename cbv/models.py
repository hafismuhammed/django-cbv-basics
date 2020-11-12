from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    genre =  models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.IntegerField()
    count = models.IntegerField(null=True, default=0)


    # for generate slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    

