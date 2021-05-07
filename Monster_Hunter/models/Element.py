from Monster_Hunter.models.Monster import Monster
from Monster_Hunter.models.Object import Object
from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Elemental_defense(models.Model):
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    element_id = models.ForeignKey(Element, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        ordering = ['object_id']
        unique_together = [["object_id", "element_id"]]


class Elemental_resistance(models.Model):
    monster_id = models.ForeignKey(Monster, on_delete=models.CASCADE)
    element_id = models.ForeignKey(Element, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        ordering = ['monster_id']
        unique_together = [["monster_id", "element_id"]]

