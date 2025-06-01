from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    discription = models.TextField()
    images = models.ImageField(upload_to='images/',null=True, blank=True)
    publishedtime = models.DateTimeField(auto_now_add=True)
    updatedtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title