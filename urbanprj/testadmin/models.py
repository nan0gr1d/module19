from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
