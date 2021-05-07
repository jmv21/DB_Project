from Monster_Hunter.models.Hunter import Hunter
from Monster_Hunter.models.Monster import Monster
from Monster_Hunter.models.Object import Object
from Monster_Hunter.models.Palico import Palico
from django.db import models




class Inventory(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['hunter_id']
        unique_together = [["hunter_id", "object_id"]]

    def __str__(self):
        return "" + self.object.name + " " + self.hunter.name + " " + str(self.quantity)

class Recipes(models.Model):
    name = models.CharField(max_length=50)
    object1 = models.ForeignKey(Object, on_delete=models.CASCADE)
    #object2 = models.ForeignKey(Object, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['object1']
        # unique_together = [["object_id1", "object_id2"]]


class Reward_object(models.Model):
    monster_id = models.ForeignKey(Monster, on_delete=models.CASCADE)
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter_id = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        ordering = ['monster_id']
        unique_together = [["object_id", "hunter_id"],["monster_id", "hunter_id"]]
