from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField

import accounts

# Create your models here.
class WatchList(models.Model):
    user = models.ForeignKey(accounts.models.User)
    show_id = JSONField()
    progress = JSONField(default={'season': 1, 'episode': 1})
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "show_id")

    def __str__(self):
        return str(self.show_id)

class Show(models.Model):
    id = models.IntegerField(primary_key=True)
    content = JSONField()
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) # Auto set date when the object is first created

    def __str__(self):
        return str(self.id)

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