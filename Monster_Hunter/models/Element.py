from Monster_Hunter.models.Monster import Monster
from Monster_Hunter.models.Object import Armor
from Monster_Hunter.models.Object import Weapon
from django.db import models
from django.core.exceptions import ValidationError


class Element(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Elemental_defense(models.Model):
    armor = models.ForeignKey(Armor, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    value = models.IntegerField()

    def clean(self):
        if(self.value <  0):
            raise ValidationError("Value field must be nonnegative")

    class Meta:
        ordering = ['armor']
        unique_together = [["armor", "element"]]

class Elemental_attack(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)

    def __str__(self):
            return self.weapon_id

    class Meta:
        ordering = ['weapon']
        unique_together = [["weapon", "element"]]

class Elemental_use(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)

    def __str__(self):
            return self.monster.name + " " + self.element.name

    class Meta:
        ordering = ['monster']
        unique_together = [["monster", "element"]]

class Elemental_resistance(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    value = models.IntegerField()

    class Meta:
        ordering = ['monster_id']
        unique_together = [["monster_id", "element_id"]]

