from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError



class Monster(models.Model):
    name = models.CharField(max_length=50)
    min_size = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    max_size = models.PositiveIntegerField(default=10, validators=[MinValueValidator(2)])
    combat_strategy = models.TextField(default="No strategy")
    rank = models.SmallIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(50)])

    def clean(self):
        if(self.min_size >= self.max_size):
            raise ValidationError("Minimum size value must be less than maximum size value")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'monsters'
        verbose_name = 'Monster'
        verbose_name_plural = 'Monsters'

