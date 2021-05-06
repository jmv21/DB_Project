from django.db import models


# Create your models here.
class Hunter(models.Model):
    name = models.CharField(max_length=50)
    experience_level = models.IntegerField()
    money = models.IntegerField(default=0)
    rank = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


