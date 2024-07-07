from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    donetask = models.BooleanField(default=False)
    user_id = models.IntegerField()

    def str(self):
        return self.title 