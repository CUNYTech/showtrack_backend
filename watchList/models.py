from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

import accounts

# Create your models here.
class WatchList(models.Model):
    user = models.ForeignKey(accounts.models.User)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    shows = ArrayField(JSONField())

    def __str__(self):
        return self.title

# class Show(models.Model):
#     show_id = models.IntegerField()
#     title = models.CharField(max_length=255)
#     desc = models.CharField(max_length=255)
#     added_at = models.DateTimeField(auto_now_add=True)
#     progress = models.IntegerField(blank=True)
#     rating = models.FloatField(blank=True)
#     list = models.ForeignKey(WatchList)

#     # change the ordering to use the order field instead of the default id

#     def __str__(self):
#         return self.title