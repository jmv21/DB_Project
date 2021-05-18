from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Hunter(models.Model):
    name = models.CharField(max_length=50)
    experience_level = models.IntegerField()
    money = models.IntegerField(default=0)
    rank = models.SmallIntegerField(default=0)

    def clean(self):
        if not(0 < self.rank <= 50):
            raise ValidationError("Rank must be from 0 to 50")
        if not(0 < self.experience_level <= 100):
            raise ValidationError("Experience level must be from 0 to 100")
    def __str__(self):
        return self.name


