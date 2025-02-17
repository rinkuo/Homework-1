from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(default="You are gay")
    image = models.ImageField(max_length=255, default=None, null=True, blank=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title
