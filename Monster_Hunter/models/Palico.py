from django.db import models
from Monster_Hunter.models.Hunter import Hunter
from django.core.exceptions import ValidationError


class Palico(models.Model):
    owner = models.ForeignKey(Hunter, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    experience_level = models.IntegerField(default=0)
    combat_style = models.SmallIntegerField(default=0)
    rank = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Palico_lent(models.Model):
    delivery_date = models.DateTimeField()
    palico = models.ForeignKey(Palico, on_delete=models.CASCADE)
    hunter_lent = models.ForeignKey(Hunter, on_delete=models.CASCADE)
    return_date = models.DateTimeField()

    def __str__(self):
        return "Lent " + self.palico.name + " to " + self.hunter_lent.name

    def clean(self):
        if(self.return_date is None or self.delivery_date is None):
            return
        if (self.return_date <= self.delivery_date):
            raise ValidationError("Delivery date can't be less or equal to return date")
        borrows = Palico_lent.objects.filter(palico_id=self.palico.id)
        for borrow in borrows:
            if (borrow.return_date > self.delivery_date or (
                    (self.delivery_date) < borrow.delivery_date > (self.delivery_date))):
                raise ValidationError("Wrong Date")
        if (self.palico.owner.id == self.hunter_lent.id):
            raise ValidationError("Can't be lend to his owner")

    class Meta:
        unique_together = [["delivery_date", "palico_id"], ["delivery_date", "hunter_lent"]]
