from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Hunter(models.Model):
    name = models.CharField(max_length=50)
    experience_level = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    money = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    rank = models.SmallIntegerField(default=0, validators=[MaxValueValidator(50), MinValueValidator(0)])

    def clean(self):
        if not (0 <= self.rank <= 50):
            raise ValidationError("Rank must be from 0 to 50")
        if not (0 <= self.experience_level <= 100):
            raise ValidationError("Experience level must be from 0 to 100")

    def __str__(self):
        return self.name
