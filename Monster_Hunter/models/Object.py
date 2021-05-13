from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


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

    class Meta:
        verbose_name_plural = "Collected Objects"


class Merchantable_Object(models.Model):
    object = models.OneToOneField(Object, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.object.name

    class Meta:
        verbose_name_plural = "Merchantable Objects"
        verbose_name = "Merchantable Object"


class Armor(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    VALUE_CHOICES = zip(range(1, 6), range(1, 6))
    armor_type = models.SmallIntegerField(default=1, choices=VALUE_CHOICES, blank=True)
    defense = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.object.name

    def clean(self):
        # if (Armor.objects.filter(object=self.object).count() != 0 and Armor.objects.get(object=self.object).armor_type!=self.armor_type):
        #     raise ValidationError("Can't be two armors types linked to the same object")
        if (self.armor_type == ''):
            raise ValidationError("Armor type must be nonnempty")

        class Meta:
            unique_together = (["object", "armor_type"])


class Weapon(models.Model):
    object = models.OneToOneField(Object, on_delete=models.CASCADE)
    VALUE_CHOICES = zip(range(1, 6), range(1, 6))
    weapon_type = models.SmallIntegerField(default=1, choices=VALUE_CHOICES, blank=True)
    damage = models.IntegerField(default=5, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.object.name

    def clean(self):
        if (Weapon.objects.filter(object=self.object).count() != 0):
            raise ValidationError("Can't be two weapons linked to the same object")
        if (self.weapon_type == ''):
            raise ValidationError("Weapon type must be nonnempty")
        if (self.damage < 1):
            raise ValidationError("Damage defense must be a greater than 1")

    class Meta:
        unique_together = [["object", "weapon_type"]]
