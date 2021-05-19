from Monster_Hunter.models.Hunter import Hunter
from Monster_Hunter.models.Monster import Monster
from Monster_Hunter.models.Object import Object
from Monster_Hunter.models.Palico import Palico
from django.db import models
from django.core.exceptions import ValidationError




class Inventory(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ['hunter_id']
        unique_together = [["hunter_id", "object_id"]]

    def __str__(self):
        return "" + self.object.name + " " + self.hunter.name + " " + str(self.quantity)

class Recipes(models.Model):
    object1 = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='object1')
    object2 = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='object2')
    quantity = models.IntegerField(default=0)

    def clean(self):
        if(self.object1.id == self.object2.id):
            raise ValidationError("The object to be created cannot be fabricated using itself in the process")
        if(self.quantity < 1):
            raise ValidationError("Quantity must be equal or greater than 1")
    def __str__(self):
        return self.object1.name

    class Meta:
       ordering = ['object1']
       unique_together = [["object1", "object2"]]


class Reward_object(models.Model):
    monster_id = models.ForeignKey(Monster, on_delete=models.CASCADE)
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter_id = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        ordering = ['monster_id']
        unique_together = [["object_id", "hunter_id"],["monster_id", "hunter_id"]]
