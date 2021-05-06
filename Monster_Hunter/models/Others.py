from Monster_Hunter.models import Hunter
from Monster_Hunter.models import Monster
from django.db import models



class Element(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Palico_lended(models.Model):
    delivery_date = models.DateTimeField()
    palico_id = models.ForeignKey(Palico, on_delete=models.CASCADE)
    hunter_lended = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    return_date = models.DateTimeField()

    def __str__(self):
        return "Lend "+ self.palico_id.name + " to " + self.hunter_lended.name

    class Meta:
        unique_together = [["delivery_date","palico_id"],["delivery_date","hunter_lended"]]

class Inventory(models.Model):
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter_id = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    class Meta:
        ordering = ['hunter_id']
        unique_together = [["hunter_id", "object_id"]]

class Recipes(models.Model):
    object_id1 = models.ForeignKey(Object, on_delete=models.CASCADE)
    #object_id_2 = models.ForeignKey(Object, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    class Meta:
        ordering = ['object_id1']
        #unique_together = [["object_id1", "object_id2"]]

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

class Reward_object(models.Model):
    monster_id = models.ForeignKey(Monster, on_delete=models.CASCADE)
    object_id = models.ForeignKey(Object, on_delete=models.CASCADE)
    hunter_id = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    class Meta:
        ordering = ['monster_id']
        unique_together = [["object_id", "hunter_id"],["monster_id", "hunter_id"]]
