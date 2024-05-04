from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    author =  models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # pupose ani kay mag sort sa post dipaly from latest post
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title # to display the title in the admin interface

