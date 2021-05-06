from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Collected_object(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    region = models.CharField(max_length=80,default="Astera")

    def __str__(self):
        return self.object.name

class Merchantable_Object(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    price = models.TextField()

    def __str__(self):
        return self.object.name

class Armor(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    armor_type = models.SmallIntegerField()
    defense = models.IntegerField(default=5)

    def __str__(self):
        return self.object.name

class Weapon(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    weapon_type = models.CharField(max_length=80)
    damage = models.IntegerField(default=5)

    def __str__(self):
        return self.object.name
