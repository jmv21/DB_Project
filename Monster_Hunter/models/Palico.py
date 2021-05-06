from django.db import models
from Monster_Hunter.models.Hunter import Hunter


class Palico(models.Model):
    owner = models.ForeignKey(Hunter,blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    experience_level = models.IntegerField(default=0)
    combat_style = models.SmallIntegerField(default=0)
    rank = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name
