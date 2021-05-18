from django.db import models
from django.core.exceptions import ValidationError


class Object(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Collected_object(models.Model):
    object = models.OneToOneField(Object, on_delete=models.CASCADE)
    region = models.CharField(max_length=80, default="Astera")

    def __str__(self):
        return self.object.name


class Merchantable_Object(models.Model):
    object = models.OneToOneField(Object, on_delete=models.CASCADE)
    price = models.TextField()

    def __str__(self):
        return self.object.name

class Armor(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    armor_type = models.SmallIntegerField()
    defense = models.IntegerField(default=5)

    def __str__(self):
        return self.object.name

    def clean(self):
       if not ( 0 < self.armor_type <= 5 ):
           raise ValidationError("Armor type must be a value between 1 and 5")
       if(self.defense < 0):
           raise ValidationError("Armor defense must be a nonnegative value")


class Weapon(models.Model):
    object = models.OneToOneField(Object, on_delete=models.CASCADE)
    weapon_type = models.CharField(max_length=80)
    damage = models.IntegerField(default=5)

    def __str__(self):
        return self.object.name

    class Meta:
        unique_together = [["object", "weapon_type"]]
