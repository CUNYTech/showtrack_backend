from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title