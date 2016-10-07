from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0) # default uses the ID to order
    course = models.ForeignKey(Course)

    # change the ordering to use the order field instead of the default id
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title