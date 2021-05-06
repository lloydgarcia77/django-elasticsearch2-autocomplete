from django.db import models

# Create your models here.

class Comments(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    name = models.CharField(max_length=200)
    postId = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.email

        
class Todo(models.Model):
    user_id = models.IntegerField()
    tid = models.IntegerField()
    title = models.CharField(max_length=200)
    completed = models.BooleanField()

    def __str__(self):
        return self.title
