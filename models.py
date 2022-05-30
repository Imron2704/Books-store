from django.db import models
from sqlalchemy import null


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    website = models.URLField()


    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/author-images', null = True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    description = models.TextField(default='')
    price = models.FloatField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/book-images', null=True)


    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title
