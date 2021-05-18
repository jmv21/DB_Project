from django.db import models



class Monster(models.Model):
    name = models.CharField(max_length=50)
    min_size = models.IntegerField(default=0)
    max_size = models.IntegerField(default=10)
    combat_strategy = models.SmallIntegerField(default=1)
    rank = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'monsters'
        verbose_name = 'Monster'
        verbose_name_plural = 'Monsters'

