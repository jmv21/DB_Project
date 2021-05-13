from Monster_Hunter.models.Hunter import Hunter
from Monster_Hunter.models.Monster import Monster
from Monster_Hunter.models.Object import Object
from Monster_Hunter.models.Palico import Palico
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


class Inventory(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])

    class Meta:
        ordering = ['hunter_id']
        unique_together = [["hunter_id", "object_id"]]
        verbose_name_plural = "Inventories"

    def clean(self):
        if not (0 < self.quantity < 999):
            raise ValidationError("Quantity must be at least 1, and less than 999 units")

    def __str__(self):
        return "" + self.object.name + " belong to " + self.hunter.name + ", quantity: " + str(self.quantity)


class Recipes(models.Model):
    object1 = models.ForeignKey(Object, on_delete=models.CASCADE)
    object2 = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='object2')
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])

    def clean(self):
        if self.object1.id == self.object2.id:
            raise ValidationError("The object to be created cannot be fabricated using itself in the process")
        if self.quantity < 1:
            raise ValidationError("Quantity must be equal or greater than 1")

    def __str__(self):
        return self.object1.name + " " + self.object2.name

    class Meta:
        ordering = ['object1']
        unique_together = [["object1", "object2"]]
        verbose_name_plural = "Recipes"


class Reward_object(models.Model):
    monster_id = models.ForeignKey(Monster, on_delete=models.CASCADE)
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return "" + self.monster_id.name + ": " + self.object_id.name

    class Meta:
        ordering = ['monster_id']
        unique_together = [["object_id", "monster_id"]]
